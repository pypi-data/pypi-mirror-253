import json
import numbers
import copy
from typing import Any, Dict, List, Optional, Union, Tuple
import concurrent.futures
import numpy as np
import pandas as pd
import folium

from pyspark.sql import DataFrame
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, ArrayType, DoubleType, StringType, MapType


from .elevation import ElevationServerEndpoint
from .overpass import OverpassServerEndpoint
from .tile import TileServerEndpoint
from .routing import RoutingServerEndpoint
from .utils import Utils, ServiceType
from .config import *


class QMap:

    WAY_TAGS = ["highway", "surface", "lanes", "maxspeed", 'crossing', 'traffic_signals']
    TAG_SEQ_ACCURACY = 0.7
    TAG_BLOCKSET={"name", "wikidata"}

    def __init__(self, api: str = "private"):
        """
        Initialize a QMap object.

        Args:
            api: The API to use ("public" or "private").
        """
        assert api in host_cfg.keys(), "The value of \"api\" parameter must be either \"public\" or \"private\""
        self._services = {}
        self._registerAll(host_cfg[api])

    def service(self, service: str):
        """
        Get the service object associated with the specified service type.

        Args:
            service: The service type.

        Returns:
            The service object associated with the specified service type.
        """
        assert ServiceType.isService(service), f"No service {service} to use"
        return self._services[service]

    def _registerAll(self, hosts):
        """
        Register all service endpoints using the provided hosts.

        Args:
            hosts: The host configuration for different services.
        """
        self._services[ServiceType.tile.value] = TileServerEndpoint(default_tile=hosts[ServiceType.tile.value])
        self._services[ServiceType.route.value] = RoutingServerEndpoint(host=hosts[ServiceType.route.value])
        self._services[ServiceType.tags.value] = OverpassServerEndpoint(host=hosts[ServiceType.tags.value])
        self._services[ServiceType.elevation.value] = ElevationServerEndpoint(host=hosts[ServiceType.elevation.value])

    def snap_to_road(self, data: Any, input_col_name: Optional[str] = None, timestamps: Any = None, radius: Any = None, tidy: bool = True, details: bool = False):
        """
        Snap the coordinates to the road.

        Args:
            data: The input data.
            input_col_name: The name of the input column.
            timestamps: Optional timestamps corresponding to the input coordinates.
            radius: Standard deviation of GPS precision used for map matching. If applicable use GPS accuracy.
            tidy: Indicates whether to tidy the output.
            details: Indicates whether to include detailed information.

        Returns:
            The snapped coordinates or detailed response.
        """
        udf_structure = StructType([
                            StructField('coordinates', ArrayType(ArrayType(DoubleType()))),
                            StructField('tags', StringType() if self.WAY_TAGS == "all" else StructType([StructField(t, ArrayType(StringType())) for t in self.WAY_TAGS])),
                            StructField('elevation', ArrayType(DoubleType()))
                        ]) if details else ArrayType(ArrayType(DoubleType()))
        return self._process_input(data, input_col_name, self._snap_to_road, udf_structure, timestamps=timestamps,radius=radius, tidy=tidy, details=details)

    def _process_input(self, data, input_col_name, func, udf_structure, **args):
        """
        Process the input data based on its type and perform the specified function.

        Args:
            data: The input data.
            input_col_name: The input column name.
            func: The function to be applied.
            udf_structure: The structure of the user-defined function (UDF).
            **args: Additional arguments for the function.

        Returns:
            The processed data.
        """
        timestamps = args.get('timestamps')
        radius = args.get('radius')

        if isinstance(data, (list, np.ndarray)):
            return func(data, **args)
    
        elif isinstance(data, pd.DataFrame):
            if isinstance(input_col_name, list):
                if isinstance(timestamps, str):
                    args['timestamps'] = data[timestamps].values
                if isinstance(radius, str):
                    args['radius'] = data[radius].values

                return func(data[input_col_name].values, **args)

            # SEQUENTIAL TASKS WITH PANDAS
            # data[col_name_cgf['outputCol']] = data.apply(lambda row: func(row[input_col_name], **Utils.update_args(row, copy.deepcopy(args))), axis=1)

            # PARALLEL TASKS WITH PANDAS
            def process_row(row, input_col_name, args):
                return func(getattr(row, input_col_name), **Utils.update_args_concurrent(row, args))
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = list(executor.map(lambda row: process_row(row, input_col_name, copy.deepcopy(args)), data.itertuples(index=False)))
            data[col_name_cgf['outputCol']] = results

            return data
        
        elif isinstance(data, DataFrame):
            if isinstance(input_col_name, list):
                raise ValueError(f"qmap supports only Batch Pyspark Processing in the current version. Look at the qsmap docs for more details")
            
            input_cols = [F.col(input_col_name)]
            if isinstance(timestamps, str):
                input_cols.append(F.col(args.pop('timestamps')))
            if isinstance(radius, str):
                input_cols.append(F.col(args.pop('radius')))

            converted_args = {key: F.lit(value) for key, value in args.items()}
            udf_func = F.udf(func, udf_structure)

            return data.withColumn(col_name_cgf['outputCol'], udf_func(*[*input_cols, *list(converted_args.values())]))

        else:  
            raise ValueError(f"Unknown {type(data)} type of the input data. qmap supports List, numpy.array, pandas.DataFrame, pyspark.sql.DataFrame in the current version")

    def _snap_to_road(self,coordinates, timestamps, radius, tidy, details) -> Any:
        """
        Internal method to snap the coordinates to the road.

        Args:
            coordinates: The input coordinates.
            timestamps: Optional timestamps corresponding to the input coordinates.
            radius: Standard deviation of GPS precision used for map matching. If applicable use GPS accuracy.
            tidy: Indicates whether to tidy the output.
            details: Indicates whether to include detailed information.

        Returns:
            The snapped coordinates or detailed response.
        """
        response = self._services[ServiceType.route.value].match(coordinates=coordinates, geometry="geojson", tidy=tidy, annotations=details,timestamps=timestamps,radius=radius)
        road = np.concatenate([sublist['geometry']['coordinates'] for sublist in response]).tolist()

        if not details:
            #return np.concatenate(list(map(lambda item: item['geometry']['coordinates'], response)))
            return None if len(road) == 0 else road
        
        if len(road) == 0: 
            return {"coordinates": None, "tags": None, "elevation": None}

        detailed_response = {}
        detailed_response['coordinates'] = road

        nodes = list(str(node) for subset in response for leg in subset.get("legs", []) for node in leg.get("annotation", {}).get("nodes", []))
        detailed_response['tags'] = self._way2tags(nodes)
        if self.WAY_TAGS == "all" and detailed_response['tags']: 
            detailed_response['tags'] = json.dumps(detailed_response['tags'])

        detailed_response['elevation'] = self._get_elevation(detailed_response['coordinates'])
        return detailed_response

    def _way2tags(self, nodes: List[str]) -> Dict:
        """
        Get tags from ways and nodes.

        Args:
            nodes: The input nodes.

        Returns:
            The dict of tags.
        """
        tags={}
        chunk_size = 600
        for start in range(0, len(nodes), chunk_size):
            chunk_nodes = nodes[start:min(start+chunk_size, len(nodes))]
            response=self._services[ServiceType.tags.value].fetch(f"""node(id:{','.join(chunk_nodes)});<;out;""")['osm'] #{"osm": {'way': [], 'node': []}}

            response['way'] = response.get('way', [])
            response['way'] = response['way'] if isinstance(response['way'], list) else [response['way']]
            ways = {}
            for way in response.get('way', []):
                nd = way.get('nd', [])
                tg = way.get('tag', [])
                nds = [n['@ref'] for n in (nd if isinstance(nd, list) else [nd]) if n]
                tgs = {t['@k']:t['@v'] for t in (tg if isinstance(tg, list) else [tg]) if t}
                ways[way['@id']] = {"node": nds, "tag": tgs}

            for iter_acc in range(13):
                selected_ways = Utils.find_ways(ways, self.TAG_SEQ_ACCURACY - (self.TAG_SEQ_ACCURACY / 14) * iter_acc, chunk_nodes)
                if selected_ways: break

            for selected_way in selected_ways:
                for k, v in ways[selected_way]['tag'].items():
                    if not any(blacklisted in k for blacklisted in self.TAG_BLOCKSET):
                        tags.setdefault(k, []).append(v)

            response=self._services[ServiceType.tags.value].fetch(f"""node(id:{','.join(chunk_nodes)});out;""")['osm']
            response['node'] = response.get('node', [])
            response['node'] = response['node'] if isinstance(response['node'], list) else [response['node']]

            for node in response.get('node', []):
                node_tags = node.get('tag', [])
                for tag in (node_tags if isinstance(node_tags, list) else [node_tags]):
                    k, v = tag.get('@k', ''), tag.get('@v', '')
                    if not any(blacklisted in k for blacklisted in self.TAG_BLOCKSET):
                        tags.setdefault(k, []).append(v)

        return self._filter_tags(tags)
    
    def _filter_tags(self, tags: Dict) -> Dict:
        """
        Filter keys in a dictionary based on WAY_TAGS.

        Args:
            tags: The input tags.

        Returns:
            The filtered tags based on WAY_TAGS.
        """
        if self.WAY_TAGS == "all":
            return tags
        elif isinstance(self.WAY_TAGS, list):
            return {key: tags.get(key, "None") for key in self.WAY_TAGS}
        else:
            print(f"Unknown WAY_TAGS={self.WAY_TAGS}")
            return None
        
    def get_elevation(self, data: Any, input_col_name: Optional[Union[str, List[str]]] = None):
        """
        Get the elevation.

        Args:
            data: The input data.
            input_col_name: The name of the input column(s).

        Returns:
            The elevation value(s).
        """
        udf_structure = DoubleType() if isinstance(input_col_name, list) else ArrayType(DoubleType())
        return self._process_input(data, input_col_name, self._get_elevation, udf_structure)
    
    def _get_elevation(self, coordinates) -> Union[float, List[float]]:
        """
        Internal method to get the elevation.

        Args:
            coordinates: The input coordinates.

        Returns:
            The elevation value(s).
        """
        response = self._services[ServiceType.elevation.value].estimate(coordinates)
        return response[0] if len(response) == 1 else response
    
    def plot_trajectory(self, data, input_col_name: Optional[Union[str, List[str]]] = None,
                        weight: int = 4, color: str = "black", opacity: float = 0.6, popup: Any = None, tile: folium.Map = None) -> folium.Map:
        """
        Plot the trajectory.

        Args:
            data: The input data.
            input_col_name: The name of the input column(s).
            weight: The weight of the polyline.
            color: The color of the polyline.
            opacity: The opacity of the polyline.
            popup: The popup content.
            tile: The tile object.

        Returns:
            The plotted tile object.
        """
        
        if isinstance(data, list):
            data = np.array(data)
        elif isinstance(data, DataFrame):
            data = data.toPandas()

        if isinstance(data, pd.DataFrame):
            if isinstance(input_col_name, list):
                data = data[input_col_name].values
            elif input_col_name:
                data = data[input_col_name]
            else:
                data = data.values

        if isinstance(data, np.ndarray):
            if len(data.shape) == 2:
                data = pd.Series(np.expand_dims(data, axis=0).tolist())
            data = pd.Series(data.tolist())

        tolist = lambda element: list(element) if isinstance(element[0], numbers.Number) else [tolist(subval) for subval in element]
        points = np.array([point for sublist in tolist(data.values) for point in sublist]).reshape(-1, 2)

        if not tile:
            tile = self._services[ServiceType.tile.value].create_tile(location=points.mean(axis=0).tolist())
        tile.fit_bounds([points.min(axis=0).tolist(), points.max(axis=0).tolist()])
        folium.PolyLine(data, weight=weight, color=color, opacity=opacity, popup=popup).add_to(tile)
        return tile
