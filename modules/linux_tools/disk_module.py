import subprocess
import json
import re

def get_disks_info():
    result = subprocess.run(['lsblk', '-d', '-o', 'MODEL,SIZE,TYPE'], capture_output=True, text=True)
    
    disks_info = []
    
    for line in result.stdout.splitlines()[1:]:  
        match = re.match(r'(.+)\s+(\S+)\s+(\S+)', line)
        if match:
            model = match.group(1).strip()
            size = match.group(2)
            device_type = match.group(3)

            size = size.replace(',', '.')

            if device_type != 'disk':
                continue

            if not model:
                continue

            size_gb = int(size[:-1]) if size[-1] == 'G' else int(size[:-1]) // 1024  # Преобразуем в ГБ
            disks_info.append({
                'model': model,
                'size': size_gb,
            })
    
    return disks_info