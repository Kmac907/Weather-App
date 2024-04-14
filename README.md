# Flask Weather App

This Flask Weather App allows users to retrieve real-time weather information by entering a city name, along with optional state and country codes. The app queries the OpenWeatherMap API to display current weather data including temperature, humidity, wind speed, and more. It's built using Flask, a lightweight WSGI web application framework.

![image](https://github.com/Kmac907/Weather-App/assets/120307903/a3bf481e-808c-4441-88cf-77b75ff99e08)

![image](https://github.com/Kmac907/Weather-App/assets/120307903/4eec149b-b687-4f6f-b235-551d04aff888)

## Features

- **User Input for Location**: Users can specify city, state, and country to accurately retrieve weather data.
- **Real-time Weather Information**: Displays current weather conditions like temperature, feels-like temperature, weather description, humidity, and wind speed.
- **Dynamic Weather Icons**: Shows icons representing current weather conditions.
- **Responsive Design**: Simple and user-friendly interface that works well on both desktop and mobile browsers.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- Flask
- Requests library

You will also need an API key from OpenWeatherMap, which you can obtain by signing up at [OpenWeatherMap](https://openweathermap.org/api).

## Installation

Follow these steps to get your development env running:

1. Clone the repository:
   `git clone https://github.com/Kmac907/Weather-App.git`

2. Navigate to the project directory:
   `cd flask-weather-app`

3. Install the required Python packages:
   `pip install flask requests`

4. Set your OpenWeatherMap API key in app.py:
   `OPENWEATHER_API_KEY = 'your_api_key_here'`
   
## Running the Application

Run the application using the Flask built-in server:
`python app.py`

## Usage

The homepage presents a form where users can enter a city, and optionally a state and country code. After submitting the form, the weather information is displayed, including details such as temperature, weather conditions, and wind speed.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## License

Distributed under the MIT License. See LICENSE for more information.




