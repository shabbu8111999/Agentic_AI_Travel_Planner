

import json

# this function finds the cheapest flight from a list of flight options
def find_cheapest_flight(from_city, to_city):

    # opening the JSON file containing flight data
    with open("data/flights.json", "r") as file:
        flights = json.load(file)

    # List to hold all matching flight options
    matched_flights = []

    # checking each flight in the JSON data
    for flight in flights:
        if flight["from"] == from_city and flight["to"] == to_city:
            matched_flights.append(flight)

    # If no flights found, return None
    if not matched_flights:
        return None
    
    # Finding the flight with the lowest price
    return min(matched_flights, key = lambda x: x["price"])