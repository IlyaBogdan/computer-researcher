from modules.SystemInformator import SystemInformator
from modules.registry.RegReader import RegReader
from modules.IPinformator import IPinformator
from modules.Reporter import Reporter
from winreg import HKEY_LOCAL_MACHINE
import urllib.request
import datetime

report = {'system': {}, 'net': {}}

keys = {
    "system_name": (HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "ProductName"),
    "release_year": (HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "ReleaseId"),
    "profile_name": (HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon", "LastUsedUsername"),
    "last_user_SID": (HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon", "AutoLogonSID"),
}

regReader = RegReader()
for key_name, path in keys.items():
    branch, hive, key = path
    report['system'][key_name] = regReader.get_value(branch, hive, key)


self_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
net_info = IPinformator(self_ip).get_info()

for key, value in net_info.items():
    report['net'][key] = value

report['date_time'] = str(datetime.datetime.now())
Reporter('http://localhost:3333/').send_report(report)