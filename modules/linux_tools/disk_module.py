import subprocess
import json

def get_disks_info():
    result = subprocess.run(['lsblk', '-o', 'NAME,MODEL,SIZE'], capture_output=True, text=True)
    
    disks_info = []
    
    for line in result.stdout.splitlines()[1:]:  
        parts = line.split()
        if len(parts) >= 3:
            name = parts[0]
            model = parts[1]
            size = parts[2]
            size_gb = int(size[:-1]) if size[-1] == 'G' else int(size[:-1]) // 1024  
            disks_info.append({
                'model': model,
                'size': size_gb,
            })
    
    return disks_info