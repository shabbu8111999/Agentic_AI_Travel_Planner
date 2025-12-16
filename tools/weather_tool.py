import requests

# this function gets weather with description
def get_weather(latitude, longitude, days):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&daily=temperature_2m_max"
        "&timezone=auto"
    )

    response = requests.get(url)
    data = response.json()

    temperatures = data["daily"]["temperature_2m_max"]

    weather_result = []

    for temp in temperatures[:days]:

        # simple weather logic
        if temp >= 32:
            description = "Hot ☀️"
        elif temp >= 25:
            description = "Pleasant 🌤️"
        else:
            description = "Cool 🌥️"

        weather_result.append({
            "temp": temp,
            "description": description
        })

    return weather_result
