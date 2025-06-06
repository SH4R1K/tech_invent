import wmi

def get_disks_info_wmi():
    c = wmi.WMI()
    disks_info = []
    for disk in c.Win32_DiskDrive():
        try:
            model = disk.Model
            size_gb = int(disk.Size) // (1024 ** 3)  
            disks_info.append({
                'model': model,
                'size': size_gb,
            })
        except:
            continue
    return disks_info
#get_disks_info_wmi()