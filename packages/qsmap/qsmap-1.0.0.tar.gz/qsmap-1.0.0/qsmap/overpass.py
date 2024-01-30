import requests
import numbers
from typing import Dict
import xmltodict
import overpy

class OverpassServerEndpoint:

    def __init__(
        self, 
        host: str = "http://overpass-api.de/api/interpreter", 
        timeout: float = 30, 
        max_retries: int = 5,
        pool_connections: int = 10,
        pool_maxsize: int = 10,
    ):
        """
        Initializes an OverpassServerEndpoint object.

        Args:
            host (str): The host URL of the Overpass API. Defaults to "http://overpass-api.de/api/interpreter".
            timeout (float): The request timeout in seconds. Defaults to 30.
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

        self._api = overpy.Overpass(url=host, max_retry_count=max_retries, retry_timeout=timeout)

        
    def fetch(self, q: str) -> Dict:
        """
        Executes an Overpass query and returns the result.

        Args:
            q (str): The Overpass query string.

        Returns:
            Dict: The result of the query.

        Raises:
            ValueError: If the response does not contain a valid code or if the osm data decoding fails.
        """
        try:
            response = self._session.get(self.host, params={"data": q}, timeout=self.timeout)
            osm_data = xmltodict.parse(response.content).get("osm", {'way': [], 'node': []})
            if not osm_data: 
                raise ValueError("No osm data in service response")
            return {"osm": osm_data}
        except Exception as error:
            print(f"Exception in OverpassServerEndpoint: {error}")
            return {"osm": {'way': [], 'node': []}}

    def query(self, q: str) -> overpy.Result:
        """
        Executes an Overpass query and returns the result.

        Args:
            q (str): The Overpass query string.

        Returns:
            overpy.Result: The result of the query.
        """
        return self._api.query(q)

