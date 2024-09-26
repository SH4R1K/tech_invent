import json
from modules.cpu_module import get_processors
from modules.mainboard import get_mainboard
from modules.ram_module import get_rams
from modules.net_module import get_network_adapters
from modules.gpu_module import get_gpus
from modules.perifery_module import get_connected_devices
def creating_file():
    collect_info_dict = {'info': {'system_info': {}}}
    collect_info_dict['info']['system_info'] = {
        'mainboard': get_mainboard(),
        "processor": get_processors(),
        "ram": get_rams(),
        "net": get_network_adapters(),
        "gpu": get_gpus(),
        "perifery": get_connected_devices()
    }
    return collect_info_dict

def main():
    dict_info = creating_file()
    with open(f'info_emae.json', 'w', encoding='utf-8') as file:
        json.dump(dict_info, file, indent=4, ensure_ascii=False)
    print("Success!")


if __name__ == "__main__":
    main()