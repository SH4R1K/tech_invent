import GPUtil
amd = True
try:
    from pyadl import *
except:
    amd = False

import wmi
def get_gpus():
    gpus = GPUtil.getGPUs()
    output = list()
    for gpu in gpus:
        try:
            output.append({
                "name": gpu.name,
                "adapter_ram": gpu.memoryTotal/1024, # gb
                "uuid": gpu.uuid,
            })
        except:
            continue;
    if (amd):
        amd_gpus = ADLManager.getInstance().getDevices()
        for gpu in amd_gpus:
            try:
                adapter_name = gpu.adapterName.decode('utf-8')
                if (all(item['name'] != adapter_name for item in output)):
                    output.append({
                        "name": adapter_name,
                    })
            except:
                continue
    return output


def get_gpu_info_wmi():
    try:
        # Создаем объект WMI
        w = wmi.WMI(namespace="root\\CIMV2")
        
        # Получаем информацию о видеокартах
        gpus = w.Win32_VideoController()
        if not gpus:
            print("No GPUs detected.")
            return
        
        for i, gpu in enumerate(gpus):
            print(f"\nGPU {i}:")
            print(f"  Name: {gpu.Name}")
            print(f"  Adapter RAM: {int(gpu.AdapterRAM) / (1024 ** 2):.2f} MB" if gpu.AdapterRAM else "  Adapter RAM: Unknown")
            print(f"  Video Processor: {gpu.VideoProcessor}")
            print(f"  Device ID: {gpu.DeviceID}")
            print(f"  PNP Device ID: {gpu.PNPDeviceID}")
            print(f"  Current Resolution: {gpu.CurrentHorizontalResolution}x{gpu.CurrentVerticalResolution}" if gpu.CurrentHorizontalResolution and gpu.CurrentVerticalResolution else "  Current Resolution: Unknown")
    except Exception as e:
        print(f"Error: {e}")

#get_gpu_info_wmi()

#print(get_gpus())