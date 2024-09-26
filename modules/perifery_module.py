import wmi

def get_connected_devices():
    c = wmi.WMI()

    devices_info = {
        "monitors": [],
        "mice": [],
        "keyboards": [],
        "printers": []
    }

    # Получение информации о мониторах
    for monitor in c.Win32_DesktopMonitor():
        print(monitor)
        devices_info["monitors"].append({
            "name": monitor.Name,
            "device_id": monitor.DeviceID,
            "screen_width": monitor.ScreenWidth,
            "screen_height": monitor.ScreenHeight
        })
    for mouse in c.Win32_PointingDevice():
        print(mouse)
        devices_info["mice"].append({
            "name": mouse.Name,
            "device_id": mouse.DeviceID
        })
    for keyboard in c.Win32_Keyboard():
        print(keyboard)
        devices_info["keyboards"].append({
            "name": keyboard.Name,
            "device_id": keyboard.DeviceID
        })
    for printer in c.Win32_Printer():
        print(printer)
        if ("PDF" not in printer.Name):
            devices_info["printers"].append({
                "name": printer.Name,
                "device_id": printer.DeviceID
            })

    return devices_info
#print(get_connected_devices())