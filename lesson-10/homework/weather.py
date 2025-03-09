import requests
api_key = "f6d55c2212059460e74de50749b9ee0b"

lat = 41.2995
lon = 69.2401

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]

print(f"Temperature:{temperature} °C\nHumidity:{humidity} %\nWeather:{description.capitalize()}")



