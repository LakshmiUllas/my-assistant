# my-assistant
import time
import datetime
import random

def greet():
    greetings = ["Hello!", "Hi there!", "Hey!", "Welcome back!"]
    return random.choice(greetings)

def get_time():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."

def get_date():
    today = datetime.date.today()
    return f"Today's date is {today.strftime('%B %d, %Y')}."

def calculate(expression):
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error in calculation: {e}"

def air_assistant():
    print("🛫 Air Assistant Activated. Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "exit":
            print("Assistant: Goodbye! Safe travels. ✈️")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Assistant:", greet())
        elif "time" in user_input:
            print("Assistant:", get_time())
        elif "date" in user_input:
            print("Assistant:", get_date())
        elif "calculate" in user_input:
            expression = user_input.replace("calculate", "").strip()
            print("Assistant:", calculate(expression))
        elif "weather" in user_input:
            print("Assistant: I'm not connected to the internet, but it's always sunny in here ☀️")
        else:
            print("Assistant: I'm not sure how to respond to that. Try asking about time, date, or calculations.")

# Run the assistant
air_assistant()
