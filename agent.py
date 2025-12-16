from tools.flight_tool import find_cheapest_flight
from tools.hotel_tool import recommend_hotel
from tools.budget_tool import calculate_budget
from tools.place_tool import get_top_places
from tools.weather_tool import get_weather
from tools.city_location import get_city_coordinates


# Main agent function to plan a trip
def travel_agent(from_city, to_city, days):

    # normalize user input
    from_city = from_city.strip().title()
    to_city = to_city.strip().title()


    flight = find_cheapest_flight(from_city, to_city)

    if flight is None:
        from tools.flight_tool import suggest_alternative_routes

        alternatives = suggest_alternative_routes(from_city)

        return {
            "error": f"No direct flight from {from_city} to {to_city}",
            "alternatives": alternatives
        }


    hotel = recommend_hotel(to_city)

    if hotel is None:
        return {"error": "No hotel available in destination city"}
    

    places = get_top_places(to_city, days)

    # get latitude and longitude for destination city
    location = get_city_coordinates(to_city)

    if location is None:
        return {"error": "Weather data not available for this city"}

    latitude, longitude = location

    # get weather data
    weather = get_weather(latitude, longitude, days)

    
    total_budget = calculate_budget(
        flight["price"],
        hotel["price_per_night"],
        days
    )

    return {
        "flight" : flight,
        "hotel" : hotel,
        "places" : places,
        "weather" : weather,
        "budget" : total_budget
    }