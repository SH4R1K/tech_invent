import subprocess

def get_memory_info():
    output = []
    
    try:
        # Выполняем команду dmidecode для получения информации о памяти
        result = subprocess.run(['sudo', 'dmidecode', '-t', 'memory'], capture_output=True, text=True, check=True)
        
        current_memory = {}
        
        for line in result.stdout.splitlines():
            line = line.strip()
            if line.startswith("Memory Device"):
                if current_memory:
                    output.append(current_memory)
                    current_memory = {}
            elif line.startswith("Manufacturer:"):
                current_memory["manufacturer"] = line.split(":", 1)[1].strip()
            elif line.startswith("Speed:"):
                current_memory["speed"] = line.split(":", 1)[1].strip()
            elif line.startswith("Size:"):
                size = line.split(":", 1)[1].strip()
                if size != "No Module Installed":
                    current_memory["capacity"] = size
            elif line.startswith("Part Number:"):
                current_memory["part_number"] = line.split(":", 1)[1].strip()
            elif line.startswith("Serial Number:"):
                current_memory["serial_number"] = line.split(":", 1)[1].strip()
            elif line.startswith("Description:"):
                current_memory["name"] = line.split(":", 1)[1].strip()
        
        # Добавляем последний модуль, если он существует
        if current_memory:
            output.append(current_memory)

    except Exception as e:
        print(f"Ошибка при получении информации о RAM: {e}")
    
    return output
