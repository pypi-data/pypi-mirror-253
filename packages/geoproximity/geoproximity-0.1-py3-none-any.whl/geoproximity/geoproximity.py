from math import radians, sin, cos, sqrt, atan2

def haversine_distance(coord1, coord2):

    # Haversine formula for great-circle distance
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radius of Earth in kilometers
    radius = 6371.0

    distance = radius * c
    return distance


def nearest_neighbor(reference_point, points):
    """
    Find the nearest neighbor among a set of geographical points.

    Parameters:
    - reference_point: reference point in degrees.
    - points: A list of tuples, each containing the latitude and longitude of a point.

    Returns:
    - Tuple containing the point and distance of the nearest point.
    """

    # Convert reference point latitude and longitude from degrees to radians
    reference_lat, reference_lon = map(radians, reference_point)

    # Initialize variables to store the index and minimum distance
    min_distance = float('inf')
    nearest_index = None

    for i, (lat, lon) in enumerate(points):
        # Convert point latitude and longitude from degrees to radians
        lat, lon = map(radians, [lat, lon])

        # Haversine formula to calculate distance
        dlat = lat - reference_lat
        dlon = lon - reference_lon

        a = sin(dlat / 2) ** 2 + cos(reference_lat) * cos(lat) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Radius of the Earth in kilometers (mean value)
        earth_radius = 6371.0

        # Calculate distance
        distance = earth_radius * c

        # Update nearest point if the current distance is smaller
        if distance < min_distance:
            min_distance = distance
            nearest_index = i

    return (points[nearest_index], min_distance)
