
import requests
import json

API_KEY = "d56c8f69033661adb7ab6298b3df2444"

city = input("Enter the city name : ")
URL = f"api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
res = requests.get(URL)
json_data = json.load(res.text)

weather = json_data["weather"][0]["description"]
temprature = json_data["main"]["temp"]
humidity = json_data["main"]["humidity"]
wind_speed = json_data["wind"]["speed"]

print(f"Weather : {weather}")
print(f"Temperature : {temprature}")
print(f"Humidity : {humidity}")
print(f"Wind speed : {wind_speed}")