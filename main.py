import streamlit as st
from agent import travel_agent

st.title("✈️ Agentic AI Travel Planner")

from_city = st.text_input("From City", "Hyderabad")
to_city = st.text_input("To City", "Goa")
days = st.slider("Number of Days", 1, 7, 3)

if st.button("Plan My Trip"):

    result = travel_agent(from_city, to_city, days)

    if result is None:
        st.error("No data found for this route")
    else:
        st.subheader("Flight Selected")
        st.write(result["flight"])

        st.subheader("Hotel Recommended")
        st.write(result["hotel"])

        st.subheader("Places to Visit")
        for place in result["places"]:
            st.write(place["name"], "-", place["rating"])

        # Weather Forecast
        st.subheader("Weather Forecast (Max Temperatures)")
        for day, temp in enumerate(result["weather"], start=1):
            st.write(f"Day {day}: {temp} °C")

        st.subheader("Estimated Budget")
        st.success(f"₹ {result['budget']}")