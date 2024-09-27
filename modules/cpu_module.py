import wmi
def get_processors():
    c = wmi.WMI()
    processors = c.Win32_Processor()
    output = list()
    for processor in processors:
        output.append({
            "name": processor.Name.strip(),
            "physical_cores": processor.NumberOfCores,
            "logical_cores": processor.NumberOfLogicalProcessors,
            "max_clock_speed": processor.MaxClockSpeed,
            "cpu_id": processor.ProcessorId
        })
    return output
#print(get_processors())
