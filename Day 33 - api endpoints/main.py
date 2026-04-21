import requests
from datetime import datetime

URL = "http://api.open-notify.org/iss-now.json"
SUNSET_URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 51.507351
MY_LONG = -0.127758

# response = requests.get(url=URL)
# response.raise_for_status()  # If not HTTP 200, raise exception
#
# data = response.json()
# # print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
#
# print(iss_position)

# ==================================================================== #
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

res = requests.get(SUNSET_URL, params=parameters)
res.raise_for_status()
sunset_data = res.json()
sunrise = sunset_data["results"]["sunrise"].split('T')[1].split(":")[0]  # Get hour from time
sunset = sunset_data["results"]["sunset"].split('T')[1].split(":")[0]

print(sunrise)

time_now = datetime.now()