import requests
import socket
import re

class ipAddr:
    def valid_addr(self, addr: str) -> bool:
        reg = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
        isValid = True
        if re.fullmatch(reg, addr):
            octets = addr.split('.')
            for octet in octets:
                if not(0 <= int(octet) <= 255):
                    isValid = False
        return isValid
    
    def is_bogon(self, addr: str) -> bool:
        bogon_range = {
            '0.0.0.0': (8, '"This" network'),
            '10.0.0.0': (8, 'Private-use network'),
            '100.64.0.0': (10, 'Carrier-grade NAT'),
            '127.0.0.0': (8, 'Loopback'),
            '127.0.0.53': (0, 'Name collision occurrence'),
            '169.254.0.0': (16, 'Link local')
        }

    def __init__(self, addr: str):
        if self.valid_addr(addr):
            self.addr = addr



class IPinformator:

    def __init__(self, host: ipAddr|str):
        reg = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
        if not(re.fullmatch(reg, host)):
            try:
                self.host = socket.gethostbyname(host)
            except Exception as e:
                print("Что-то пошло не так")                
        else:
            self.host = host
    
    def get_info(self) -> dict:
        response = requests.get(f'http://ipinfo.io/{self.host}/json')
        data = response.json()
        try:
            data['hostname'] = socket.gethostbyaddr(self.host)
        except:
            pass
        try:
            data['loc'] = {
                'x': data['loc'].split(',')[0],
                'y': data['loc'].split(',')[1]
            }
            del data['readme']
        except:
            pass
        
        return data