import psutil
import cpuinfo
def get_processors():
    my_cpuinfo = cpuinfo.get_cpu_info()
    output = list()
    output.append({
            "name": my_cpuinfo["brand_raw"],
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
            "max_clock_speed": int(psutil.cpu_freq().max)
        })
    return output
#print(get_processors())
