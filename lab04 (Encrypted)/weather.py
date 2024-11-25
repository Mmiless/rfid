import requests
import json

# WeatherAPI key
WEATHER_API_KEY = 'cdc445714ebe4de79ca214022242309'  # TODO: Replace with your own WeatherAPI key
base_url = 'http://api.weatherapi.com/v1'


def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    request_url = '{}/current.json?key={}&q={}'.format(base_url, WEATHER_API_KEY, city)
    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(request_url)
    
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad #Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        weather = json.loads(json.dumps(response.json(), indent = 4))            
        
        # TODO: Display the extracted weather information in a well-formatted manner.
        print("Status 200: OK")
        print(f"Weather data for {city}...")
        print("Temperature: " + str(weather['current']['temp_f']) + chr(176) 
              + "F (Feels like: " + str(weather['current']['feelslike_f']) + chr(176) + "F)")
        print("Condition: " + str(weather['current']['condition']['text']))
        print("Humidity: " + str(weather['current']['humidity']) + "%")
        print("Wind: " + str(weather['current']['wind_mph']) + " mph, Direction: " 
              + str(weather['current']['wind_dir']))
        print("Atmospheric pressure: " + str(weather['current']['pressure_mb']) + "mb")
        print("UV index value: " + str(weather['current']['uv']))
        print("Cloud cover: " + str(weather['current']['cloud']) + "%")
        print("Visibility: " + str(weather['current']['vis_miles']) + " miles")
    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        if response.status_code == 400:
            print(f"Error: {response.status_code}. Bad Request.")
        elif response.status_code == 401:
            print(f"Error: {response.status_code}. Unauthorized Request.")
        elif response.status_code == 403:
            print(f"Error: {response.status_code}. Forbidden Request.")
        elif response.status_code == 404:
            print(f"Error: {response.status_code}. Not found.")
        else:
            print(f"Error: {response.status_code}. Something went wrong.")


if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input('City name: ')
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
