from modules.SystemInformator import SystemInformator
from modules.registry.RegReader import RegReader
from modules.IPinformator import IPinformator
from winreg import HKEY_LOCAL_MACHINE


keys = {
    "System name": (HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "ProductName"),
    "Release year": (HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "ReleaseId"),
    "Profile name": (HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon", "LastUsedUsername"),
    "Last User SID": (HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon", "AutoLogonSID"),
}

regReader = RegReader()
for key_name, path in keys.items():
    branch, hive, key = path
    print("{0}: {1}".format(key_name, regReader.get_value(branch, hive, key)))

net_info = IPinformator('10.168.190.160').get_info()

print("\nNet information")
for key, value in net_info.items():
    print("{0}: {1}".format(key, value))