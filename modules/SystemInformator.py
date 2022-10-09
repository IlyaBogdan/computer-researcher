import psutil
import json
from platform import uname

# this class gives general information about system
class SystemInformator:
    # information about operation system
    def system_info(self) -> dict:
        info = uname()
        return  {
                'system_name': info.system,
                'comp_name': info.node,
                'OS version': info.version,
                'arhitecture': info.machine
        }
    # information about processor on this machine
    def processor_info(self) -> dict:
        return {
                'processor_name': uname().processor,
                'cpu_count': psutil.cpu_count(logical=False),
                'min_freq': '{} MHz'.format(psutil.cpu_freq().min),
                'max_freq': '{} MHz'.format(psutil.cpu_freq().max)
        }
    # information about RAM
    def RAM_info(self) -> dict:
        info = psutil.virtual_memory()
        return {
            'total': '{} MB'.format(round(info.total/(2**20))),
            'available': '{} MB'.format(round(info.available/(2**20))),
        }
    #information about disks
    def disk_usage(self) -> dict:
        disks = psutil.disk_partitions()
        memory = {}
        for disk in disks:
            disk_name = disk.device
            disk_info = psutil.disk_usage(disk_name)
            memory[disk_name.replace("\\", '')] = {
                'total': '{} MB'.format(round(disk_info.total/(2**20))),
                'used': '{} MB'.format(round(disk_info.used/(2**20))),
                'free': '{} MB'.format(round(disk_info.free/(2**20)))
            }
        return memory

    # all information
    def general_info(self) -> dict:
        return {
            'system': self.system_info(),
            'processor': self.processor_info(),
            'RAM': self.RAM_info(),
            'memory': self.disk_usage()
        }