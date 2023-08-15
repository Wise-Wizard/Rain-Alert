import requests
API_KEY = "27795ce922e262e40fe837a780a624e1"
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat=12.971599&lon=77.594566&appid={API_KEY}")
print(weather_data.json())
