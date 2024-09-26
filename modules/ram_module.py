import wmi
from .memory_converter import correct_size
def get_rams():
    c = wmi.WMI()
    rams = c.Win32_PhysicalMemory()
    output = dict()
    for i, ram in enumerate(rams):
        output[i] = {
            "name": ram.Name.strip(),
            "manufacturer": ram.Manufacturer,
            "speed": ram.Speed,
            "capacity": correct_size(int(ram.Capacity)),
            "memory_type": ram.MemoryType
        }
    return output
#print(get_rams())