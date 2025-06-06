import requests
def send_data(json, api_url = "http://localhost:5239"):
    url = api_url + "/api"
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(f"{url}/Invent", data=json, headers=headers)
    if (response.status_code == 200):
        print("Успех")
    else:
        print(f"Сервер вернул код: {response.status_code}")
        print("Проверьте правильность ссылки на API и повторите попытку")