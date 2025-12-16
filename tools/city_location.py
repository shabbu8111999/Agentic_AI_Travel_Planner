# this dictionary stores latitude and longitude for cities
CITY_LOCATION = {
    "Goa": (15.2993, 74.1240),
    "Hyderabad": (17.3850, 78.4867),
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Kolkata": (22.5726, 88.3639),
    "Jaipur": (26.9124, 75.7873)
}

# this function returns lat and long for a city
def get_city_coordinates(city):
    return CITY_LOCATION.get(city, None)
