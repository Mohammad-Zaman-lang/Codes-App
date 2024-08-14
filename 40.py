40
import tkinter as tk
from tkinter import ttk
# import requests

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")

        # API key (get your own from https://openweathermap.org/)
        self.api_key = "YOUR_API_KEY"

        # City entry
        city_label = ttk.Label(master, text="Enter City:")
        city_label.pack(pady=10)

        self.city_entry = ttk.Entry(master)
        self.city_entry.pack()

        # Fetch button
        fetch_button = ttk.Button(master, text="Fetch Weather", command=self.fetch_weather)
        fetch_button.pack(pady=10)

        # Weather information display
        self.weather_info_label = ttk.Label(master, text="", font=("Arial", 16))
        self.weather_info_label.pack()

    def fetch_weather(self, requests=None):
        city = self.city_entry.get()
        if city:
            try:
                # API call
                api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
                response = requests.get(api_url)
                response.raise_for_status()  # Raise an exception for bad status codes
                # 
                # Parse data
                data = response.json()
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"]

                # Display weather information
                self.weather_info_label.config(text=f"Weather in {city}:\nTemperature: {temp}°C\nDescription: {description}")

            except requests.exceptions.RequestException as e:
                self.weather_info_label.config(text=f"Error: {e}")
        else:
            self.weather_info_label.config(text="Please enter a city name.")

# Create the main window and run the app
root = tk.Tk()
app = WeatherApp(root)
root.mainloop()

