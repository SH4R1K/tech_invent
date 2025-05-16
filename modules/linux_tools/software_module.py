import subprocess
import re

def get_installed_packages():
    output = []
    try:
        # Выполняем команду rpm для получения информации о пакетах
        result = subprocess.run(['rpm', '-qa', '--qf', '%{NAME}-%{VERSION}-%{RELEASE}\n'], capture_output=True, text=True, check=True)
        
        for line in result.stdout.splitlines():
            if line:
                package_name, package_version = line.rsplit('-', 2)[:-2], line.rsplit('-', 2)[-2:]
                package_name = '-'.join(package_name)
                package_version = '-'.join(package_version)
                package_info = get_package_info(package_name)
                output.append({
                    "name": package_name,
                    "version": package_version,
                    "manufacturer": package_info
                })
    except Exception as e:
        print(f"Ошибка при получении установленных пакетов: {e}")
    
    return output

def get_package_info(package_name):
    try:
        # Выполняем команду rpm для получения информации о пакете
        result = subprocess.run(['rpm', '-qi', package_name], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if re.match(r'^\s*Vendor:\s*(.*)', line):
                return re.match(r'^\s*Vendor:\s*(.*)', line).group(1).strip()
            elif re.match(r'^\s*Packager:\s*(.*)', line):
                return re.match(r'^\s*Packager:\s*(.*)', line).group(1).strip()
    except Exception as e:
        print(f"Ошибка при получении информации о пакете {package_name}: {e}")
    
    return "Unknown"