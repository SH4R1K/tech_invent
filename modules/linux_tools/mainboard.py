import subprocess
def getBaseboardProductName():
        output = subprocess.check_output("sudo dmidecode -t 2 | grep 'Manufacturer\|Product\|Serial'", shell=True, text=True)
        lines = {}
        for line in output.strip().split('\n'):
            key, value = line.split(': ', 1)
            lines[key.strip()] = value.strip()
        return lines


def get_mainboard():
    mainboard_info = getBaseboardProductName()
    output = list()
    output.append({
            "name": f"{mainboard_info['Manufacturer']} {mainboard_info['Product Name']}",
            "serial_number": mainboard_info["Serial Number"]
    })
print(getBaseboardProductName())