from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    state = request.form.get('state', '').strip()
    country = request.form.get('country', '').strip()
    location_query = f"{city},{state},{country}".strip(',')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={location_query}&appid={OPENWEATHER_API_KEY}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        weather_info = {
            'city': weather_data.get('name'),
            'state': state,  # Pass the state to the template
            'country': weather_data['sys'].get('country'),
            'temperature': weather_data['main']['temp'],
            'feels_like': weather_data['main']['feels_like'],
            'weather': weather_data['weather'][0]['main'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed']
        }
        return render_template('weather.html', weather=weather_info)
    else:
        return jsonify({'error': 'Weather data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

