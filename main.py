import json, sys
from platform import uname
from modules import info_collector as ic
sys.path.append('modules/linux_tools')
sys.path.append('modules/windows_tools')
sys.path.append('modules')
from api.api_module import send_data
def creating_file():
    collect_info_dict = {'name':'','workplace': {'hardware_info': {},'software':{}}}
    collect_info_dict['name'] = '0109'
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
        "perifery": info_collector.tools.get_connected_devices()
    }
    collect_info_dict['workplace']['software'] = info_collector.tools.get_installed_software()
    return collect_info_dict

def main():
    dict_info = creating_file()
    with open(f'info_emae.json', 'w', encoding='utf-8') as file:
        json.dump(dict_info, file, indent=4, ensure_ascii=False)
        jsons = json.dumps(dict_info)
        try:
            print('Zaglushka')
            send_data(jsons)
        except:
            print('api is dead ☠️')
    print("Success!")


if __name__ == "__main__":
    main()