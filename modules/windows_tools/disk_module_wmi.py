import wmi

def get_disks_info_wmi():
    c = wmi.WMI()
    disks_info = []
    for disk in c.Win32_DiskDrive():
        model = disk.Model
        size_gb = int(disk.Size) // (1024 ** 3)  
        print(disk)
        disks_info.append({
            'model': model,
            'size': size_gb,
        })
    return disks_info
get_disks_info_wmi()