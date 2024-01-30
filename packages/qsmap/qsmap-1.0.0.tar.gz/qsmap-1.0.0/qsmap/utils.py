import numbers
from typing import Dict, Union
import enum


class Utils:

    @staticmethod
    def encode_val(value) -> Union[str, numbers.Number]: 
        """
        Encodes the given value to a string.

        Args:
            value: The value to encode.

        Returns:
            str or numeric: The encoded value.
        """
        return str(value).lower() if isinstance(value, (bool, str)) else value

    @staticmethod
    def update_args(row, args, keys=['timestamps', 'radius']) -> Dict:
        """
        Update the given arguments.

        Args:
            row: The value to be taken.
            args: The dict to update.
            keys: The keys to update.

        Returns:
            dict: Updated arguments
        """
        args.update({key: row[args[key]] for key in keys if isinstance(args.get(key), str)})
        return args
    
    @staticmethod
    def update_args_concurrent(row, args, keys=['timestamps', 'radius']) -> Dict:
        """
        Update the given arguments in concurrent race.

        Args:
            row: The value to be taken.
            args: The dict to update.
            keys: The keys to update.

        Returns:
            dict: Updated arguments
        """
        args.update({key: getattr(row, args[key]) for key in keys if isinstance(args.get(key), str)})
        return args
    
    @staticmethod
    def find_ways(ways, threshold, nodes):
        """
        Find the most appropriate ways.

        Args:
            ways: The input ways.
            threshold: The threshold used to filter out the ways.
            nodes: The input nodes.

        Returns:
            list: Selected ways
        """
        selected_ways = []
        for way_id, way_data in ways.items():
            intersection_size = max(0.001, len(set(way_data['node']) & set(nodes)))
            way_node_count = len(set(way_data['node']))
            nodes_count = len(set(nodes))

            precision = intersection_size / nodes_count
            recall = intersection_size / way_node_count

            f_beta_score = (1 + intersection_size**2) * (precision * recall) / (intersection_size**2 * precision + recall)

            if f_beta_score > threshold:
                selected_ways.append(way_id)
        
        return selected_ways


class ServiceType(enum.Enum):
    """
    Enum class representing different service types.
    """
    tile = "tile"
    route = "route"
    tags = "tags"
    elevation = "elevation"

    @classmethod
    def isService(cls, value: str) -> bool:
        """
        Check if the given value is a valid service type.

        Args:
            value: The value to check.

        Returns:
            True if the value is a valid service type, False otherwise.
        """
        return any(value == member.name for member in cls)