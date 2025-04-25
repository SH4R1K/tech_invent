import requests
def send_data(json, api_url = "http://localhost:5239"):
    url = api_url + "/api"
    #print(json)
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(f"{url}/Invent", data=json, headers=headers)
    print(response.status_code)
    print(response.text)