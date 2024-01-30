from .utils import ServiceType

col_name_cgf={
    'outputCol':'outputCol',
    'outputLatCol': 'outputLatCol',
    'outputLonCol': 'outputLonCol',
    'outputElevCol': 'outputElevCol',
    'inputLatLocCol': 'inputLatLocCol'
}

host_cfg={
    "public": {
        ServiceType.tile.value: "OpenStreetMap",
        ServiceType.route.value: "http://router.project-osrm.org",
        ServiceType.tags.value: "http://overpass-api.de/api/interpreter",
        ServiceType.elevation.value: "https://api.opentopodata.org"
    },
    "private": {
        ServiceType.tile.value: "QS OSM Bright",
        ServiceType.route.value: "https://map-routing.ds.questarauto.com",
        ServiceType.tags.value: "https://map-overpass.ds.questarauto.com/api/interpreter",
        ServiceType.elevation.value: "https://map-elevation.ds.questarauto.com"
    }
}