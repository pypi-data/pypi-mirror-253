import folium

class TileServerEndpoint:

    TILES_CFG = {
        "QS Klokantech Basic": 'https://map-tile.ds.questarauto.com/styles/klokantech-basic/{z}/{x}/{y}.png',
        "QS OSM Bright": 'https://map-tile.ds.questarauto.com/styles/osm-bright/{z}/{x}/{y}.png',
        "OpenStreetMap": "OpenStreetMap",
        "Stamen Terrain": "Stamen Terrain",
        "Stamen Toner": "Stamen Toner",
        "Stamen Watercolor": "Stamen Watercolor",
        "CartoDB positron": "CartoDB positron",
        "CartoDB dark_matter": "CartoDB dark_matter"
    }

    def __init__(self, default_tile: str = "OpenStreetMap"):
        """
        Initializes a TileServerEndpoint object.

        Args:
            default_tile (str): The default tile server to use. Defaults to "OpenStreetMap".
        """
        self.default_tile = default_tile

    def create_tile(
        self,
        tiles: str = None,
        location: list[float] = [31.4117, 35.0818],
        zoom_start: float = 9.0,
        **kwargs
    ) -> folium.Map:
        """
        Creates a tile map using Folium library.

        Args:
            tiles (str): The tile server to use. Defaults to None, which uses the default_tile value.
            location (list[float]): The geographic coordinates of the center of the map. Defaults to [31.4117, 35.0818] (Israel).
            zoom_start (float): The initial zoom level of the map. Defaults to 9.0.
            **kwargs: Additional keyword arguments accepted by the folium.Map function.

        Returns:
            folium.Map: A Folium map object.

        Raises:
            Exception: If the specified tiles server is not found in TILES_CFG dictionary.
            Exception: If any unexpected error occurs during map creation.
        """
        tiles = tiles or self.default_tile
        try:
            return folium.Map(
                tiles=self.TILES_CFG[tiles],
                attr=tiles,
                location=location,
                zoom_start=zoom_start,
                **kwargs
            )
        except KeyError:
            print(f"KeyError in TileServerEndpoint. No '{tiles}' tile to use")
            return folium.Map(tiles="OpenStreetMap")
        except Exception as error:
            print(f"Exception in TileServerEndpoint: {error}")
            return folium.Map(tiles="OpenStreetMap")