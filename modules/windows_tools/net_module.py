import wmi
def get_network_adapters():
    c = wmi.WMI()
    network_adapters = c.Win32_NetworkAdapter()
    output = list()
    for nw_adapter in network_adapters:
        if (nw_adapter.PhysicalAdapter and nw_adapter.NetConnectionStatus == 2):
            if not any(keyword in nw_adapter.Name 
                       for keyword in ["Virtual", "Oracle", "Hyper-V", "VPN", "Pseudo", "sing-tun", "Tunnel"]):
                output.append({
                    "name": nw_adapter.Name,
                    "manufacturer": nw_adapter.Manufacturer,
                    "mac_address": nw_adapter.MACAddress,
                    "adapter_type": nw_adapter.AdapterType
                })
    return output
#print(get_network_adapters())