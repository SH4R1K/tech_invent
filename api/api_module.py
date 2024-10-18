import requests
def send_data(json):
    url = "http://localhost:5239/api"
    response = requests.post(f"{url}/Invent", json=json)
    print(response.status_code)