import tkinter as tk
from datetime import datetime
import requests
import config

defaultFont = ("Ubuntu", 20)

# Function to update the label with current date and time
def update_datetime():
    current_datetime = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    datetime_label.config(text=current_datetime)
    # Schedule the next update after 1000 milliseconds (1 second)
    root.after(1000, update_datetime)

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city):
    api_key = config.API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# Function to update weather label with fetched data
def update_weather_label():
    city = "New York"  # Example city
    weather_data = fetch_weather_data(city)
    print(weather_data)
    if "weather" in weather_data and "main" in weather_data:
        weather = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        weather_label.config(text=f"Weather: {weather}, Temperature: {temperature}°C")
    else:
        weather_label.config(text="Weather data not available")

# Create the main application window
root = tk.Tk()
root.title("Bot")

# Set the size of the window
root.geometry("800x600")  # Width x Height
root.configure(bg="#0091ff")

# Create a label widget
label = tk.Label(root, text="Hello, World!", bg="#0091ff")
label.configure(font = defaultFont)

# datetime label
datetime_label = tk.Label(root, text="", font=("Ubuntu", 15), bg="#0091ff")
datetime_label.pack(pady=5, anchor="ne")
update_datetime()

# Create a label widget for weather
weather_label = tk.Label(root, text="", font=("Ubuntu", 15), bg="#1d0074", fg="white")
weather_label.pack(pady=5, anchor="nw")

# Button to update weather
update_button = tk.Button(root, text="Update Weather", command=update_weather_label)
update_button.pack(pady=5)

# Define a function to be called when the button is clicked
def button_click():
    label.config(text="It works!")

# Start the Tkinter event loop
root.mainloop()