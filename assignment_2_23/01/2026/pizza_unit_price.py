import math

def pizza_unit_price(diameter_cm, price_usd):
    """
    Calculates and returns the unit price of a pizza per square meter.
    """
    # Convert diameter from centimeters to meters
    diameter_m = diameter_cm / 100
    radius = diameter_m / 2

    # Calculate area of the pizza (m^2)
    area = math.pi * radius ** 2

    # Calculate and return unit price
    return price_usd / area


def check_pizza_unit_price():
    """
    Main program: asks user for input and compares two pizzas.
    """
    diameter1 = float(input("Enter diameter of pizza 1 (cm): "))
    price1 = float(input("Enter price of pizza 1 (USD): "))

    diameter2 = float(input("Enter diameter of pizza 2 (cm): "))
    price2 = float(input("Enter price of pizza 2 (USD): "))

    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    print(f"Pizza 1 unit price: {unit_price1:.2f} USD/m²")
    print(f"Pizza 2 unit price: {unit_price2:.2f} USD/m²")

    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


# ---- Program starts here ----
check_pizza_unit_price()
