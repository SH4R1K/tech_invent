class InfoCollector:
    def __init__(self, os):
        self.os = os
        if os == 'windows':
            from windows_tools.WindowsTools import WindowsTools as wt
            self.tools = wt()
        else: 
            from windows_tools.WindowsTools import WindowsTools as wt
            self.tools = wt()