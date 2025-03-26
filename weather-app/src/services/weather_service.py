import requests
import logging

# Configura el logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, city):
        
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        
        response = requests.get(self.base_url, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error fetching weather data: {response.status_code}, Response: {response.text}")
            return None