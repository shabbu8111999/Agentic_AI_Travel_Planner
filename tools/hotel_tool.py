

import json

# This function finds the cheapest hotel from a list of hotel options
def recommend_hotel(city):

    # opening the JSON file containing hotel data
    with open("data/hotels.json", "r") as file:
        hotels = json.load(file)

    # Filtering hotels based on the specified city
    city_hotels = []
    for hotel in hotels:
        if hotel["city"] == city:
            city_hotels.append(hotel)

    # If no hotels found, return None
    if not city_hotels:
        return None
    
    # Sorting by stars (descending) and then by price (ascending)
    city_hotels.sort(key=lambda x: (-x["stars"], x["price_per_night"]))
    return city_hotels[0]