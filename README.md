# Инвентаризация Linux с dnf менеджером пакетов
### Установить PIP
```sh
sudo dnf install python3-pip
```
### Установить зависимости
```sh
pip install -r requirements_linux.txt
```
### Запустить программу
```sh
python main.py --api_url API_URL --cabinet CABINET_NAME
```