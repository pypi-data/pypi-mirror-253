import json
from math import radians

def calculate_polygon_area(geojson_data):
    """
    Calculate the area of a polygon defined in GeoJSON format.

    Parameters:
    - geojson_str: GeoJSON string representing the polygon.

    Returns:
    - Area of the polygon in square km.
    """
    try:
        # Extract coordinates from GeoJSON
        if 'geometry' in geojson_data and 'coordinates' in geojson_data['geometry']:
            polygon_coords = geojson_data['geometry']['coordinates'][0]
        else:
            raise ValueError("Invalid GeoJSON format. Please provide a GeoJSON string with a 'Polygon' geometry.")

        # Convert coordinates to radians
        coords_rad = [(radians(lat), radians(lon)) for lon, lat in polygon_coords]

        # Calculate polygon area
        area = 0.5 * abs(sum(x0*y1 - x1*y0 for (x0, y0), (x1, y1) in zip(coords_rad, coords_rad[1:] + [coords_rad[0]])))

        # Radius of the Earth in kilometers (mean value)
        earth_radius = 6371.0

        # Convert area to square kilometers
        area_km2 = area * earth_radius**2

        return round(area_km2, 3)

    except json.JSONDecodeError:
        raise ValueError("Invalid GeoJSON format. Please provide a valid GeoJSON string.")