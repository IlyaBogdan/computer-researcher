import requests
import socket
import re

class IPinformator:

    def valid_addr(self, addr: str) -> bool:
        reg = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
        isValid = True
        if re.fullmatch(reg, addr):
            octets = addr.split('.')
            for octet in octets:
                if not(0 <= int(octet) <= 255):
                    isValid = False
        return isValid
    
    def __init__(self, host: str):
        reg = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
        if not(re.fullmatch(reg, host)):
            try:
                self.host = socket.gethostbyname(host)
            except Exception as e:
                print("Что-то пошло не так")                
        else:
            if self.valid_addr(host):
                self.host = host
    
    def get_info(self) -> dict:
        response = requests.get(f'http://ipinfo.io/{self.host}/json')
        data = response.json()
        try:
            data['hostname'] = socket.gethostbyaddr(self.host)
        except Exception as e:
            pass
        data['loc'] = {
            'x': data['loc'].split(',')[0],
            'y': data['loc'].split(',')[1]
        }
        del data['readme']
        return data
