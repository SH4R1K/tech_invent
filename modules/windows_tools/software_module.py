import winreg

def get_software_info(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    ignore_keywords = ["Update", "Redistributable", "Runtime", "Support", "Assistant", "Help", "Driver"]

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            if any(keyword in software['name'] for keyword in ignore_keywords):
                continue 

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['vendor'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['vendor'] = 'undefined'

            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list

def get_installed_software():
    software_list = (
        get_software_info(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) +
        get_software_info(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) +
        get_software_info(winreg.HKEY_CURRENT_USER, 0)
    )
    return software_list