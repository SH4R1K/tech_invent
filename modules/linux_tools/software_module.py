import subprocess

def get_installed_packages():
    output = []
    try:
        # Выполняем команду dpkg для получения информации о пакетах
        result = subprocess.run(['dpkg', '-l'], capture_output=True, text=True, check=True)
        
        for line in result.stdout.splitlines()[5:]:  # Пропускаем первые 5 строк
            parts = line.split()
            if len(parts) >= 3:
                package_name = parts[1]
                package_version = parts[2]
                # Получаем информацию о производителе
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
        # Выполняем команду apt-cache для получения информации о пакете
        result = subprocess.run(['apt-cache', 'show', package_name], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if line.startswith("Maintainer:"):
                return line.split(":", 1)[1].strip()
    except Exception as e:
        print(f"Ошибка при получении информации о пакете {package_name}: {e}")
    
    return "Unknown"