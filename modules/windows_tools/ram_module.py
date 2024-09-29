import wmi, sys
from memory_converter import correct_size
def get_rams():
    c = wmi.WMI()
    rams = c.Win32_PhysicalMemory()
    output = list()
    for ram in rams:
        #print(ram)
        output.append({
            "name": ram.Name.strip(),
            "manufacturer": ram.Manufacturer,
            "speed": ram.Speed,
            "capacity": correct_size(int(ram.Capacity)),
            "memory_type": ram.MemoryType,
            "part_number": ram.PartNumber.strip(),
            "serial_number": ram.SerialNumber
        })
    return output
#print(get_rams())