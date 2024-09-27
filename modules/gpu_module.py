import GPUtil
from .memory_converter import correct_size
def get_gpus():
    gpus = GPUtil.getGPUs()
    output = list()
    for gpu in gpus:
        output.append({
            "name": gpu.name,
            "adapter_ram": gpu.memoryTotal/1024, # gb
            "uuid": gpu.uuid,
        })
    return output
#print(get_gpus())