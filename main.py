import requests
from twilio.rest import Client
account_sid = 'AC04697766eb497dd5a9b3d405ac874a63'
auth_token = '[AuthToken]'
API_KEY = "27795ce922e262e40fe837a780a624e1"
OMW_API = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": API_KEY
}
weather_data = requests.get(OMW_API, params=weather_params)
current_weather = weather_data.json()['weather'][0]['main']
if (current_weather == "Rain" or current_weather == "Drizzle" or current_weather == "Thunderstorm"):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain today! Bring your Umbrella☔",
        to='+917406320038',
        from_='+17069819153'
    )

