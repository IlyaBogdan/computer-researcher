from typing import Literal
from winreg import *
from ..SystemInformator import SystemInformator

# this class works with windows registry
class RegReader:
    def __init__(self, computer_name=None):
        if not(computer_name): # if computer name not defined. I want to add posible to execute this script on remote machine
            self.computer_name = SystemInformator().system_info()['comp_name']
        else:
            self.computer_name = computer_name
        
    # information about some hive
    def hive_desc(self, branch: HKEYType, hive: Literal) -> list:
        connected_branch = ConnectRegistry(self.computer_name, branch)
        connected_hive = OpenKey(connected_branch, hive)
        keys = []
        i = 0
        while True:
            try:
                n = EnumValue(connected_hive, i)
                keys.append(n)
                i += 1
            except:
                break
        CloseKey(connected_hive)
        return keys

    
    def get_value(self, branch: HKEYType, hive: Literal, key: str) -> str:
        connected_hive = OpenKeyEx(branch, hive)
        value = QueryValueEx(connected_hive, key)
        CloseKey(connected_hive)
        return value[0]


    # delete some key from regisrty
    def delete_key(self, branch, key) -> None:
        pass

    # create some key in regisrty
    def create_key(self, branch: HKEYType, path: Literal, endpoint: str) -> None:
        hive = OpenKeyEx(branch, path)
        new_key = CreateKey(hive, endpoint)

    def set_value(self, branch: HKEYType, path: Literal, key: str, value: str) -> None:
        pass
