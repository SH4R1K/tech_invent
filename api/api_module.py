import requests
def send_data(json):
    url = "http://sh4r1k.ru:52081/api"
    response = requests.post(f"{url}/Invent", json=json)
    print(response.status_code)