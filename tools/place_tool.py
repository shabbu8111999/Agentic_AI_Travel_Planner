

import json

# This function gives a recommendation for a place to visit in a specified city
def get_top_places(city, days):

    # opening the JSON File containing place data
    with open ("data/places.json", "r") as file:
        places = json.load(file)

    # filtering places based on the specified city
    city_places = []
    for place in places:
        if place["city"] == city:
            city_places.append(place)

    # sorting places by rating (descending) and then by popularity (descending)
    city_places.sort(key=lambda x: x["rating"], reverse=True)

    return city_places[:days]