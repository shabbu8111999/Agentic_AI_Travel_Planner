import streamlit as st
from agent import travel_agent
from tools.flight_tool import get_available_cities

st.title("✈️ Travel Planner Agent")

cities = get_available_cities()

from_city = st.selectbox("From City", cities)
to_city = st.selectbox("To City", cities)

days = st.slider("Number of Days", 1, 7, 3)

if st.button("Plan My Trip"):

    result = travel_agent(from_city, to_city, days)

    if "error" in result:
        st.error(result["error"])

        if "alternatives" in result and result["alternatives"]:
            st.info("Available destinations from this city:")
            for city in result["alternatives"]:
                st.write("➡️", city)


    else:
        st.subheader("Flight Selected")
        st.write(result["flight"])

        st.subheader("Hotel Recommended")
        st.write(result["hotel"])

        st.subheader("Places to Visit")
        for place in result["places"]:
            st.write(place["name"], "-", place["rating"])

        # Weather Forecast
        st.subheader("Weather Forecast")

        for day, weather in enumerate(result["weather"], start=1):
            st.write(
                f"Day {day}: {weather['description']} ({weather['temp']} °C)"
            )

        st.subheader("Estimated Budget")
        st.success(f"₹ {result['budget']}")