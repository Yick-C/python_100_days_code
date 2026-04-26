import requests
import os
from twilio import *

DAILY_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
FIVE_DAY_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": "51.507351",
    "lon": "-0.127758",
    "appid": api_key,
    "cnt": 4
}

response = requests.get(FIVE_DAY_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for weather in weather_data["list"]:
    weather_code = weather["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It's going to rain today. Bring an umbrella",
    #     from_="+12345678901",
    #     to="+441234567890",
    # )
    print("Bring an umbrella.")