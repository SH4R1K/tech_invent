import json, sys
import argparse
from platform import uname
from modules import info_collector as ic
sys.path.append('modules/linux_tools')
sys.path.append('modules/windows_tools')
sys.path.append('modules')
from api.api_module import send_data
def creating_file(cabinet_name):
    collect_info_dict = {'name':'','workplace': {'hardware_info': {},'software':{}}}
    collect_info_dict['name'] = cabinet_name
    collect_info_dict['workplace'] = {
        'comp_name': uname().node,
        'os_name': f"{uname().system} {uname().release}",
        'version': uname().version
    }
    info_collector = ic.InfoCollector(uname().system.lower())
    collect_info_dict['workplace']['hardware_info'] = {
        'mainboard': info_collector.tools.get_mainboard(),
        "processor": info_collector.tools.get_processors(),
        "ram": info_collector.tools.get_rams(),
        "net": info_collector.tools.get_network_adapters(),
        "gpu": info_collector.tools.get_gpus(),
        "disk": info_collector.tools.get_disk_info()
    }
    collect_info_dict['workplace']['software'] = info_collector.tools.get_installed_software()
    return collect_info_dict

def main(cabinet_name, api_url):
    if (cabinet_name == None):
        print("Кабинет не определён")
        cabinet_name = "Не определённый"
    if (api_url == None):
        print("Укажите ссылку на API")
        return
    dict_info = creating_file(cabinet_name)
    with open(f'info_emae.json', 'w', encoding='utf-8') as file:
        json.dump(dict_info, file, indent=4, ensure_ascii=False)
        jsons = json.dumps(dict_info)
        try:
            print('Zaglushka')
            send_data(jsons, api_url)
        except:
            print('api is dead ☠️')
    print("Success!")


if __name__ == "__main__":
    # Парсим аргументы командной строки
    parser = argparse.ArgumentParser(description="Get submission.")

    parser.add_argument(
        "--cabinet",
        type=str,
        help="Cabinet name",  # Путь к папке с аудиофайлами
    )
    parser.add_argument(
        "--api_url",
        type=str,
        help="API url",  # Путь для сохранения результатов
    )
    args = parser.parse_args()
    main(args.cabinet, args.api_url)