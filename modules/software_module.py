import wmi

def get_installed_software():
    c = wmi.WMI()
    software_list = []
    for product in c.Win32_Product():
        print(product)
        software_list.append({
            "name": product.Name,
            "version": product.Version,
            "vendor": product.Vendor
        })

    return software_list

print(get_installed_software())