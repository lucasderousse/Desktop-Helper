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
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    return data

# Function to update weather label with fetched data
def update_weather_label():
    city = "St. Louis"  # Example city
    weather_data = fetch_weather_data(city)
    # print(weather_data) <= used to print json
    if "weather" in weather_data and "main" in weather_data:
        weather = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        weather_label.config(text=f"{city}: {weather.capitalize()},\nTemperature: {temperature}°F")
    else:
        weather_label.config(text="Weather data not available")
    root.after(300000, update_weather_label)

# Create the main application window
root = tk.Tk()
root.title("Bot")

# Set the size of the window
root.geometry("800x600")  # Width x Height
root.configure(bg="#0091ff")

# Style configuration
button_bg = "#4CAF50"  # Green background color
button_fg = "white"     # White text color
button_font = ("Helvetica", 12, "bold")  # Font settings
button_relief = tk.RAISED  # Raised border appearance
button_borderwidth = 3     # Border width

# Create a label widget
label = tk.Label(root, text="Hello, World!", bg="#0091ff")
label.configure(font = defaultFont)

# datetime label
datetime_label = tk.Label(root, text="", font=("Ubuntu", 15), bg="#0091ff")
datetime_label.pack(pady=5, anchor="ne")
update_datetime()

# Create a label widget for weather
weather_label = tk.Label(root, text="", font=("Ubuntu", 15), bg="#0091ff", fg="white")
weather_label.pack(pady=5, anchor="ne")

# Button to update weather
update_button = tk.Button(root, text="Update Weather", command=update_weather_label, bg=button_bg, fg=button_fg, font=button_font, relief=button_relief, borderwidth=button_borderwidth)
update_button.pack(pady=5, anchor="ne")

# Start the Tkinter event loop
root.mainloop()