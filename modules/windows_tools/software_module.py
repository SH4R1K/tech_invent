import wmi

def get_installed_software():
    c = wmi.WMI()
    software_list = []
    for product in c.Win32_Product():
        software_list.append({
            "name": product.Name,
            "version": product.Version,
            "vendor": product.Vendor
        })
    return software_list