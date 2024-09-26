import wmi
def get_mainboard():
    c = wmi.WMI()
    motherboards = c.Win32_BaseBoard()
    output = dict()
    for i, motherboard in enumerate(motherboards):
        output[i] = {
            "name": f"{motherboard.Manufacturer} {motherboard.Product}",
            "serial_number": motherboard.SerialNumber
        }
    return output
#print(get_mainboard())