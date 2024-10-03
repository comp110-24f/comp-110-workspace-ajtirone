# Write a function called get_weather_report that takes no inputs and returns a str
# It should use the input function to ask the user “What is the weather?” and save that as the local variable weather
# If weather is "rainy" or "cold", it should print "Bring a jacket!"
# If weather is "hot", it should print "Keep cool out there!"
# Otherwise, it should print "I don't recognize this weather."
# return the weather variable


def get_weather_report() -> str:
    """display weather instructions"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
