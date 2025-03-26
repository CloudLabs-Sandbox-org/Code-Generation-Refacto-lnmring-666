from flask import Flask, render_template, request
from services.weather_service import WeatherService

app = Flask(__name__)
weather_service = WeatherService(api_key='a2ac2b745c7a55ba04abd1232d2177df')

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None
    if request.method == 'POST':
        city = request.form.get('city')
        api_response = weather_service.fetch_weather(city)
        if api_response:
            weather_data = {
                'city': api_response.get('name'),
                'temperature': api_response['main'].get('temp'),
                'humidity': api_response['main'].get('humidity'),
                'conditions': api_response['weather'][0].get('description')
            }
        else:
            error_message = "Could not retrieve weather data. Please check the city name and try again."
    return render_template('index.html', weather=weather_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)