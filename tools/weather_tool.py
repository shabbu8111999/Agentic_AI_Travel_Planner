import requests

# This function fetches the current weather for a given city
def get_weather(latitude, longitude, days):

    # open-meteo API endpoint
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&daily=temperature_2m_max,weathercode"
        "&timezone=auto"
    )

    # sending GET request to the API
    response = requests.get(url)

    # converting response to JSON
    data = response.json()

    # getting max temperature for the specified number of days
    temperatures = data["daily"]["temperature_2m_max"]

    return temperatures[:days]