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

            # Конвертируем размер в GB и затем в int
            if size[-1] == 'G':
                size_gb = int(float(size[:-1]))  # Конвертируем в float, затем в int
            elif size[-1] == 'T':
                size_gb = int(float(size[:-1]) * 1024)  # Конвертируем TB в GB и затем в int
            else:
                size_gb = int(float(size[:-1]) / 1024)  # Конвертируем MB в GB и затем в int

            disks_info.append({
                'model': model,
                'size': size_gb,
            })
    
    return disks_info
