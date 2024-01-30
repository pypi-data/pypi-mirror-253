# qsmap Package

`qsmap` is a Python package that provides convenient functions for working with geographical data, routing services, elevation data, and map visualization. It simplifies the process of interacting with various services and APIs related to geographic information, allowing users to perform common tasks easily.

### Features
- Snap coordinates to the nearest road
- Get elevations for the given coordinates
- Plot trajectories on interactive maps

**More details are on the Confluence page.**

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install qsmap.

```bash
pip install qsmap
```

## Usage

Here are some examples of how to use QMap package:

### Snap Coordinates to Road
```python
from qsmap import QMap

qmap = QMap()

data = [[32.005013, 34.78869], [32.005003, 34.788822], [32.004992, 34.788953], [32.004985, 34.7891]]
result = qmap.snap_to_road(data, details=True)

print(result)
```

### Get Elevation Data
```python
from qsmap import QMap

qmap = QMap()

data = [[32.005013, 34.78869], [32.005003, 34.788822], [32.004992, 34.788953]]
result = qmap.get_elevation(data)

print(result)
```

### Plot Trajectory on Map
```python
from qsmap import QMap

qmap = QMap()

data = [[32.005013, 34.78869], [32.005003, 34.788822], [32.004992, 34.788953]]
qmap.plot_trajectory(data)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)