from tools.flight_tool import find_cheapest_flight
from tools.hotel_tool import recommend_hotel
from tools.budget_tool import calculate_budget
from tools.place_tool import get_top_places
from tools.weather_tool import get_weather


# Main agent function to plan a trip
def travel_agent(from_city, to_city, days):

    flight = find_cheapest_flight(from_city, to_city)
    hotel = recommend_hotel(to_city)
    places = get_top_places(to_city, days)

    # latitude and longitude for weather fetching (dummy values for example)
    latitude = 15.2993
    longitude = 74.1240

    weather = get_weather(latitude, longitude, days)

    if flight is None or hotel is None:
        return None
    
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