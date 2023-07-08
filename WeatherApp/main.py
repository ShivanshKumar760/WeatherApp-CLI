import argparse
import pyfiglet
import requests
from simple_chalk import chalk
# api key for openweathermap

API_KEY = "67445566b8cf5466a6d3d3621aef4983"
# Base URL for API call
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# Map the weather codes to weather icons
MAP_ICON = {
    '01d': '☀️',
    '02d': '⛅️',
    '03d': '☁️',
    '04d': '☁️',
    '09d': '🌧',
    '10d': '🌦',
    '11d': '⛈',
    '13d': "❄️",
    '50d': "🌫",
    #Night Icon
    '01n': '🌑',
    '02n': '🌫️',
    '03n': '☁️',
    '04n': '🌩️',
    '09n': '🌧',
    '10n': '🌦',
    '11n': '⛈',
    '13n': "❄️",
    '50n': "🌫",

}
city = input('Enter city name: ')
#create a url variable
url = f'{BASE_URL}?q={city}&appid={API_KEY}'

# url= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
#make a request to the API
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Sorry, there was a problem retrieving the weather information"))
    print(chalk.red("Please try again later"))
    exit()
#parsing the json response from api and extract the weather inofrmation
data = response.json()
#get information from the response
temprature= data['main']['temp']
feels_like= data['main']['feels_like']
description = data['weather'][0]['description']
icon = data['weather'][0]['icon']
city= data['name']
country = data['sys']['country']

#construct the output with weather icons
weather_icon= MAP_ICON.get(icon, '')
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output+=f"{weather_icon} {description}\n\n"
output+=f"Temprature: {temprature-273.15}°C\n"
output+=f"Feels like: {feels_like-273.15}°C\n"
print(chalk.green(output))
