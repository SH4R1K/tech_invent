from .cpu_module import get_processors
from .mainboard import get_mainboard
from .ram_module import get_memory_info
from .net_module import get_network_adapters
from .gpu_module import get_gpus
from .perifery_module import get_connected_devices
from .software_module import get_installed_packages
from .disk_module import get_disks_info
class LinuxTools:
    def __init__(self):
        print("Linux!!!")

    def get_processors(self):
        return get_processors()
    
    def get_mainboard(self):
        return get_mainboard()
    
    def get_rams(self):
        return get_memory_info()
    
    def get_network_adapters(self):
        return get_network_adapters()
    
    def get_gpus(self):
        return get_gpus()
    
    def get_connected_devices(self):
        return get_connected_devices()
    
    def get_installed_software(self):
        return get_installed_packages()
    
    def get_disk_info(self):
        return get_disks_info() 