import subprocess
import json
import re

def get_disks_info():
    result = subprocess.run(['lsblk', '-o', 'NAME,MODEL,SIZE'], capture_output=True, text=True)
    
    disks_info = []
    
    for line in result.stdout.splitlines()[1:]:  
        match = re.match(r'(\S+)\s+(.*)\s+(\S+)', line)
        if match:
            name = match.group(1)
            model = match.group(2)
            size = match.group(3)
            size_gb = int(size[:-1]) if size[-1] == 'G' else int(size[:-1]) // 1024  # Преобразуем в ГБ
            disks_info.append({
                'model': model,
                'size': size_gb,
            })
    
    return disks_info