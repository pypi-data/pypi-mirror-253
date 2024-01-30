import requests
import numbers
from typing import List
from itertools import chain
import numpy as np


class ElevationServerEndpoint:
    def __init__(
        self,
        host: str = "https://api.opentopodata.org",
        version: str = "v1",
        timeout: float = 5,
        max_retries: int = 5,
        pool_connections: int = 10,
        pool_maxsize: int = 10,
    ):
        """
        Initializes an ElevationServerEndpoint object.

        Args:
            host (str): The host URL of the elevation server. Defaults to "https://api.opentopodata.org".
            version (str): The version of the elevation API. Defaults to "v1".
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

    def _decode_response(self, response) -> List:
        """
        Decodes the response received from the elevation server.

        Args:
            response: The response object.

        Returns:
            list: The decoded response.

        Raises:
            Exception: If the response does not contain a valid status.
        """
        try:
            response = response.json()
            if ("status" not in response) or ("OK" not in response.get("status", {})):
                raise ValueError(f"No valid response. Response={response}")
            return [result["elevation"] for result in response["results"]]
        except Exception as error:
            print(f"Exception in ElevationServerEndpoint: {error}")
            return [None]

    def estimate(self, coordinates, dataset: str = "mapzen") -> List:
        """
        Estimates the elevation for the given coordinates using the specified dataset.

        Args:
            coordinates: The input coordinates.
            dataset (str): The dataset to use. Defaults to "mapzen".

        Returns:
            list: The decoded response from the elevation server.
        """
        if np.ndim(coordinates) == 1:
            coordinates = np.expand_dims(coordinates, axis=0)
        
        if len(coordinates) > 500:
            return list(chain.from_iterable(map(self.estimate, np.array_split(coordinates, 2))))

        params = {  
            "locations": "|".join(map(lambda coord: f"{coord[0]},{coord[1]}", coordinates))
        }
        url = f"{self.host}/{self.version}/{dataset}"
        return self._decode_response(self._session.get(url, params=params, timeout=self.timeout))

