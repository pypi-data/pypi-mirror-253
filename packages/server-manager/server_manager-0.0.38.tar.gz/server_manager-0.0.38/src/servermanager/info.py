import platform
import os
import datetime
import math
import psutil
import json


def proc():
    proclist = os.popen('ps aux').read().split('\n')
    procDict = {}
    titles = proclist[0].strip().split(" ")
    proclist.pop(0)
    proclist.pop()
    
    while "" in titles:
        titles.remove("")

    for i in titles:
        procDict.update({i: []})

    for i in proclist:
        data = i.split(" ")

        while "" in data:
            data.remove("")

        #prin(data)

        for j in range(len(titles)):
            procDict[titles[j]].append(data[j])
    
    

    #for i in proclist:
    #    for j in i.split(" "):
    #        procDict.update({j: proclist[1:]})

    return procDict

class system_dynamic:
    def __init__(self):
        try:
            self.clock_speeds = os.popen('cat /proc/cpuinfo | grep "cpu MHz"').read().replace("cpu MHz", "").replace(":", "").strip().split("\n")
            self.round_clock_speeds = [round(float(x) / 1000, 1) for x in self.clock_speeds]
            self.average_clock_speed = round(sum(map(float, self.clock_speeds)) / len(self.clock_speeds) / 1000, 1)
            self.found_cpu = True
        except:
            self.clock_speeds = ["Not found"]
            self.round_clock_speeds = ["Not found"]
            self.found_cpu = False
        self.cpu_usage = psutil.cpu_percent()
        self.cpu_core_usage = psutil.cpu_percent(percpu=True)
        self.core_info = {
            "lenght": len(self.clock_speeds),
            "clock_speeds": self.round_clock_speeds
        }
        self.python_version = platform.python_version()
        self.uptime = os.popen('uptime -p').read()
        self.systime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.used_memory = f'{round(psutil.virtual_memory().used / 1024 / 1024 )} Mb'
        self.used_swap = f'{round(psutil.swap_memory().used / 1024 / 1024 )} Mb'
        self.used_memory_percent = f'{round(psutil.virtual_memory().percent, 2)}'
        self.used_swap_percent = f'{round(psutil.swap_memory().percent, 2)}'
        self.upload_speed = f'{round(psutil.net_io_counters().bytes_sent / 1024 / 10)}'
        self.download_speed = f'{round(psutil.net_io_counters().bytes_recv / 1024 / 10)}'
    
    def get_json(self):
        data = { 
            "cpu_usage": self.cpu_usage,
            "cpu_core_usage": self.cpu_core_usage, 
            "average_clock_speed": self.average_clock_speed,
            "core_info": self.core_info,
            "python_version": self.python_version,
            "uptime": self.uptime,
            "systime": self.systime,
            "used_memory": self.used_memory,
            "used_swap": self.used_swap,
            "used_memory_percent": self.used_memory_percent,
            "used_swap_percent": self.used_swap_percent,
            "upload_speed": self.upload_speed,
            "download_speed": self.download_speed,
        }
        
        if self.found_cpu == True:
            data.update({"clock_speeds": self.clock_speeds})
            data.update({"round_clock_speeds": self.round_clock_speeds})

        return json.dumps(data)
        

class system_static:

    def __init__(self):
        self.os_name = os.popen('cat /etc/os-release | grep "PRETTY_NAME"').read().replace("PRETTY_NAME=", "").replace("\"", "").replace("\n", "")
        self.hostname = platform.node()
        self.os_version = platform.version()
        self.os_release = platform.release()
        self.machine = platform.machine()
        self.processor = platform.processor()
        self.memory = f'{round(psutil.virtual_memory().total / 1024 / 1024 / 1024)} Gb'
        self.swap = f'{round(psutil.swap_memory().total / 1024 / 1024 / 1024)} Gb'
        self.network_interfaces = os.popen('ip link show | grep BROADCAST | awk \'{print $2}\' | cut -d ":" -f 1').read().strip().split("\n")
        self.disks = json.loads(os.popen('lsblk -J').read())
        self.partitions = []
        for i in self.disks["blockdevices"]:
            try:
                for j in i['children']:
                    self.partitions.append(j)
            except:
                pass
        #prin(self.partitions)

        if not self.processor:
            cpuname = os.popen('cat /proc/cpuinfo | grep "model name"').readlines()[0].replace("model name", "").replace(":", "").replace("\n", "").strip()
            self.processor = cpuname

    def get_json(self):
        data = {
            "os_name": self.os_name,
            "hostname": self.hostname,
            "os_version": self.os_version,
            "os_release": self.os_release,
            "machine": self.machine,
            "processor": self.processor,
            "memory": self.memory,
            "swap": self.swap,
            "disks": self.disks,
            "disks_count": len(self.disks["blockdevices"]),
            "partitions": self.partitions
        }

        return json.dumps(data)
