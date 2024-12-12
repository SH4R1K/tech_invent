import requests
def send_data(json, api_url = "http://localhost:5239"):
    url = api_url + "/api"
    response = requests.post(f"{url}/Invent", json=json)
    print(response.status_code)