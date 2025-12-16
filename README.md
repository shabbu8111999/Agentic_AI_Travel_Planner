# ✈️ Agentic AI-Based Travel Planning Assistant

This project is developed as part of my **internship (Project 3)**. It demonstrates how an **Agentic AI system** can automatically plan a travel itinerary using structured datasets, simple decision-making logic, and a Streamlit user interface.

The project follows a **traditional, step-by-step software development approach**, making it easy to understand, explain, and extend.

---

## 📌 Problem Statement

Planning a trip usually requires checking multiple websites for:

* Flights
* Hotels
* Tourist places
* Weather
* Budget estimation

This manual process is time-consuming and error-prone. The goal of this project is to build an **AI-based travel assistant** that:

* Automatically selects flights and hotels
* Suggests places to visit
* Shows weather conditions
* Estimates the total travel budget

---

## 🎯 Project Objectives

* Use **realistic JSON datasets** for flights, hotels, and places
* Implement an **agent-based workflow** (tools + decision logic)
* Integrate a **free weather API (Open-Meteo)**
* Build a **user-friendly Streamlit interface**
* Prevent user errors using dropdowns and suggestions

---

## 🛠️ Tech Stack Used

* **Python** – Core programming language
* **uv** – Modern Python package & environment manager
* **Streamlit** – Web interface
* **JSON** – Structured datasets
* **Requests** – API calls (weather)

---

## ⚙️ Environment Setup (Using `uv`)

This project uses **uv instead of traditional venv** for simplicity and faster dependency management.

### Step 1: Initialize the project

```bash
uv init
```

### Step 2: Install required packages

```bash
uv add streamlit requests
```

> `uv` automatically manages the environment, so no manual activation is needed.

---

## 📦 requirements.txt

Although `uv` is used, a `requirements.txt` file is included for internship and deployment standards.

```txt
streamlit
requests
```

---

## 📁 Project Folder Structure

```
Agentic_AI_Travel_Planner/
│
├── data/
│   ├── flights.json
│   ├── hotels.json
│   └── places.json
│
├── tools/
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   ├── places_tool.py
│   ├── budget_tool.py
│   ├── weather_tool.py
│   └── city_location.py
│
├── agent.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Datasets Used

### Flights Dataset (`flights.json`)

* Source city
* Destination city
* Airline
* Price
* Departure & arrival time

### Hotels Dataset (`hotels.json`)

* Hotel name
* City
* Star rating
* Price per night
* Amenities

### Places Dataset (`places.json`)

* Place name
* City
* Type (park, beach, fort, etc.)
* Rating

All datasets are stored locally and read using Python.

---

## 🧠 Agentic Architecture (How the System Works)

The project follows a **tool-based agent design**:

1. User selects cities and trip duration
2. Agent calls individual tools:

   * Flight Tool → selects cheapest flight
   * Hotel Tool → selects best-rated hotel
   * Places Tool → selects top attractions
   * Weather Tool → fetches weather using API
   * Budget Tool → calculates total cost
3. Agent combines results into a final trip plan

This mimics how a **human travel agent reasons step by step**.

---

## 🌦️ Weather Integration

* Uses **Open-Meteo Free API** (no API key required)
* City-to-latitude/longitude mapping is handled using a dictionary
* Raw temperatures are converted into user-friendly descriptions:

  * Hot ☀️
  * Pleasant 🌤️
  * Cool 🌥️

---

## 🖥️ Streamlit User Interface

Key UI features:

* Dropdowns populated from dataset (prevents wrong input)
* Automatic destination suggestions
* Alternative routes shown if no direct flight exists
* Clean, minimal, and easy-to-use layout

---

## ▶️ How to Run the Project

```bash
uv run streamlit run main.py
```

Then open the browser link shown in the terminal.

---

## ✅ Error Handling & Improvements

* Case normalization for city names
* Dropdowns instead of free text input
* Friendly error messages
* Alternative route suggestions when direct flights are unavailable

---

## 📈 Final Output

The system generates:

* Selected flight details
* Recommended hotel
* Day-wise places to visit
* Weather forecast with description
* Estimated total travel budget

---

## 🧪 Example Use Case

**From:** Hyderabad
**To:** Goa
**Days:** 3

Output includes flight, hotel, places, weather, and budget in one screen.

---

## 🏁 Conclusion

This project demonstrates how **Agentic AI concepts** can be applied using simple Python logic and structured data. It avoids unnecessary complexity while maintaining clean architecture and real-world relevance.

The system is **internship-ready, explainable, and scalable**.

---

## 📌 Future Enhancements

* LangChain ReAct Agent
* Multi-city travel planning
* Database integration
* API-based real-time flight data

---

**Developed as part of Internship – Project 3**