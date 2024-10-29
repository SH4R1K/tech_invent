import subprocess
import json

def get_disks_info_powershell():
    disks_info = []
    try:
        command = [
            "powershell", "-Command",
            "Get-PhysicalDisk | Select-Object DeviceID, MediaType, Size, Model | ConvertTo-Json"
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        disks = json.loads(result.stdout)

        for disk in disks:
            disk_type = disk["MediaType"]
            model = disk["Model"]
            size_gb = int(disk["Size"]) // (1024 ** 3)  # Размер в ГБ
            disks_info.append({
                'type': disk_type,
                'model': model,
                'size': size_gb
            })
    except Exception as e:
        print(f"Ошибка при получении информации о дисках: {e}")
    return disks_info