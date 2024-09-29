import wmi
def get_mainboard():
    c = wmi.WMI()
    motherboards = c.Win32_BaseBoard()
    output = list()
    for motherboard in motherboards:
        output.append({
            "name": f"{motherboard.Manufacturer} {motherboard.Product}",
            "serial_number": motherboard.SerialNumber
        })
    return output
#print(get_mainboard())