import wmi
def get_mainboard():
    c = wmi.WMI()
    motherboards = c.Win32_BaseBoard()
    for motherboard in motherboards:
        output = {
            "name": f"{motherboard.Manufacturer} {motherboard.Product}",
            "serial_number": motherboard.SerialNumber
        }
    return output
#print(get_mainboard())