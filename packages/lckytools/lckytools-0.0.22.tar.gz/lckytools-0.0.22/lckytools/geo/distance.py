import math


def haversine(latitude1, longitude1, latitude2, longitude2):
    # Radius of the Earth in meters
    earth_radius = 6371000

    # Convert degrees to radians
    phi1 = math.radians(latitude1)
    phi2 = math.radians(latitude2)
    delta_phi = math.radians(latitude2 - latitude1)
    delta_lambda = math.radians(longitude2 - longitude1)

    # Haversine formula
    chord_length_squared = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    )
    angular_distance = 2 * math.atan2(
        math.sqrt(chord_length_squared), math.sqrt(1 - chord_length_squared)
    )

    return earth_radius * angular_distance  # Distance in meters
