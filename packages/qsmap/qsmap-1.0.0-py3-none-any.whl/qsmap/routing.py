import requests
import json
import numbers
from typing import List, Union
import numpy as np 
import polyline

from .utils import Utils


class RoutingServerEndpoint:

    RESPONSE_KEYS_CFG = {
        "match": "matchings",
        "route": "routes"
    }

    def __init__(
        self,
        host: str = "http://router.project-osrm.org",
        version: str = "v1",
        profile: str = "driving",
        timeout: float = 5,
        max_retries: int = 5,
        pool_connections: int = 10,
        pool_maxsize: int = 10,
    ):
        """
        Initializes a RoutingServerEndpoint object.

        Args:
            host (str): The host URL of the routing server. Defaults to "http://router.project-osrm.org".
            version (str): The version of the routing API. Defaults to "v1".
            profile (str): The routing profile to use. Defaults to "driving".
            timeout (float): The request timeout in seconds. Defaults to 5.
            max_retries (int): The maximum number of retries for failed requests. Defaults to 5.
            pool_connections (int): The number of pool connections. Defaults to 10.
            pool_maxsize (int): The maximum size of pool. Defaults to 10.

        Raises:
            AssertionError: If the timeout value is not a number.
            AssertionError: If the max_retries value is not an integer or less than 1.
        """
        assert isinstance(timeout, numbers.Number), "Invalid timeout value"
        assert isinstance(max_retries, int) and max_retries >= 1, "Invalid max_retries value"

        self.host = host
        self.version = version
        self.profile = profile
        self.timeout = timeout
        self.max_retries = max_retries
        self.pool_connections = pool_connections
        self.pool_maxsize = pool_maxsize

        self._session = requests.Session()
        self._adapter = requests.adapters.HTTPAdapter(
            pool_connections=self.pool_connections,
            pool_maxsize=self.pool_maxsize,
            max_retries=self.max_retries)
        self._session.mount("http://", self._adapter)
        self._session.mount("https://", self._adapter)

    def _decode_response(self, response, service: str, params: dict) -> List:
        """
        Decodes the response received from the routing server.

        Args:
            response: The response object.
            service (str): The routing service used.
            params (dict): The request parameters.

        Returns:
            list: The decoded response.

        Raises:
            ValueError: If the response does not contain a valid code or if the geometry decoding fails.
        """
        try:
            response = response.json()
            if ("code" not in response) or ("Ok" not in response["code"]):
                raise ValueError(f"No valid response. Response={response}")

            if self.RESPONSE_KEYS_CFG[service] in response:

                geometry_processing_method = "decode" if params["geometries"] in ("polyline", "polyline6") else "flip"

                for item in response[self.RESPONSE_KEYS_CFG[service]]:

                    geometry = item.get("geometry")

                    if geometry is None: 
                        raise ValueError(f"No geometry found to decode")

                    if geometry_processing_method == "decode":
                        item["geometry"] = {"coordinates": np.array(polyline.decode(geometry))}
                    else:
                        item["geometry"] = {"coordinates": np.flip(geometry["coordinates"], axis=1)}
            else:
                raise ValueError(f"No {service} service found to decode")
            
            return response[self.RESPONSE_KEYS_CFG[service]]
        except Exception as error:
            print(f"Exception in RoutingServerEndpoint: {error}")
            return [{"geometry": {"coordinates": []}}]

    def match(
        self,
        coordinates,
        steps: bool = False,
        overview: str = "full",
        geometry: str = "polyline6",
        timestamps: list = None,
        radius: list = None,
        annotations: Union[bool,str] = False,
        gaps: str = "ignore",
        tidy: bool = False,
        waypoints: list = None,
    ) -> List:
        """
        Finds the best match for a set of input coordinates.

        Args:
            coordinates : The input coordinates.
            steps (bool): Whether to return step-by-step instructions. Defaults to False.
            overview (str): The level of overview geometry to be returned. Defaults to "full".
            geometry (str): The type of geometry to use in the response. Defaults to "polyline".
            timestamps (list): Optional timestamps corresponding to the input coordinates.
            radius (list): Standard deviation of GPS precision used for map matching. If applicable use GPS accuracy.
            annotations (bool or str): Whether to include additional metadata in the response. Defaults to False.
            gaps (str): Allows the input track splitting based on huge timestamp gaps between points. Defaults to "ignore".
            tidy (bool): Allows the input track modification to obtain better matching quality for noisy tracks. Defaults to False.
            waypoints (list): Treats input coordinates indicated by given indices as waypoints in returned Match object.

        Returns:
            list: The decoded response from the routing server.
        """
        service = "match"
        params = {
            "steps": Utils.encode_val(steps),
            "overview": overview,
            "geometries": geometry,
            "timestamps": ";".join(map(str, timestamps)) if timestamps is not None else timestamps,
            "radiuses": ";".join(map(str, radius)) if radius is not None else radius,
            "annotations": Utils.encode_val(annotations),
            "gaps": gaps,
            "tidy": Utils.encode_val(tidy),
            "waypoints": waypoints,
        }

        url = f"{self.host}/{service}/{self.version}/{self.profile}/{';'.join(map(lambda coord: f'{coord[1]},{coord[0]}', coordinates))}"
        return self._decode_response(self._session.get(url, params=params, timeout=self.timeout), service, params)
