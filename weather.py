import requests

def get_weather(api_key, location, unit='metric'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={unit}'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        return weather
    else:
        print("Error fetching weather data:", data['message'])
        return None

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    location = input("Enter city name or ZIP code: ")
    unit = input("Enter preferred unit (metric/imperial): ").lower()

    weather = get_weather(api_key, location, unit)
    if weather:
        print("\nWeather Information:")
        print(f"Temperature: {weather['temperature']} °{'C' if unit == 'metric' else 'F'}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description']}")

if __name__ == "__main__":
    main()
