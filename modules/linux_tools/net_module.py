import psutil

def get_network_adapters():
    output = []
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    banword = ["Virtual", "Oracle", "Hyper-V", "VPN", "Pseudo"]
    for interface_name, interface_addresses in interfaces.items():
        if not any(keyword in interface_name 
                       for keyword in banword):
            if stats[interface_name].isup:
                mac_address = None
                for addr in interface_addresses:
                    if addr.family == psutil.AF_LINK:
                        mac_address = addr.address
                        break
                
                output.append({
                    "name": interface_name,
                    "manufacturer": "Unknown",
                    "mac_address": mac_address.replace('-',':'),
                    "adapter_type": "Ethernet" if "eth" in interface_name else "Wireless" if "wlan" in interface_name else "Other"
                })
    return output

print(get_network_adapters())
