# this function calculates the total budget based on individual expenses
def calculate_budget(flight_price, hotel_price, days):

    # average daily food and travel expenses
    daily_cost = 800

    total = flight_price + (hotel_price * days) + (daily_cost * days)

    return total