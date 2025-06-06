import subprocess
def getBaseboardProductName():
    try:
        output = subprocess.check_output(f"sudo dmidecode -t 2 | grep 'Manufacturer\\|Product\\|Serial'", shell=True, text=True)
        lines = {}
        for line in output.strip().split('\n'):
            key, value = line.split(': ', 1)
            lines[key.strip()] = value.strip()
        return lines
    except:
        return None


def get_mainboard():
    mainboard_info = getBaseboardProductName()
    if (mainboard_info != None):
        output = {
                "name": f"{mainboard_info['Manufacturer']} {mainboard_info['Product Name']}",
                "serial_number": mainboard_info["Serial Number"]
        }
    return output
#print(getBaseboardProductName())