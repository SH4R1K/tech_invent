import requests
def send_data(json):
    url = "http://localhost:5132"
    response = requests.post(f"{url}/WeatherForecast", json=json)
    print(response.status_code)