import requests
url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=url)
response.raise_for_status()  # If not HTTP 200, raise exception

data = response.json()
# print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)