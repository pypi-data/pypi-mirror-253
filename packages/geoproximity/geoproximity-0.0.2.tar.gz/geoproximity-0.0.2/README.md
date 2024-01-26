### GeoProximity Package Usage Guide

#### Introduction

GeoProximity is a Python package designed to facilitate geospatial distance calculations, point projections, and related operations. It includes functions for both Haversine distance (great-circle distance) and Euclidean distance calculations. GeoProximity is suitable for applications that require proximity analysis, spatial operations, and basic geospatial functionality.

#### Installation

Ensure Python is installed on your system, then install the `geoproximity` package using `pip`:

```sh
pip install geoproximity
```

#### Calculate harversine distance
```python
import geoproximity
geoproximity.haversine_distance(coord1, coord2)
```
It returns the haversine distance between two points in km.

#### Find the nearest neighbor from the list of coordinates to the referece point
```python
geoproximity.nearest_neighbor(reference_point, coordinates_list)
```
It returns a tuple containing the nearest point and distance of the nearest point from the reference point in km.

Example:
```python
reference_point = (37.7749, -122.4194)
other_points = [(34.0522, -118.2437), (40.7128, -74.0060), (41.8781, -87.6298)]

nearest_point, min_distance = geoproximity.nearest_neighbor(reference_point, other_points)

```
