import requests

class Reporter:

    def __init__(self, host: str):
        self.host = host

    def send_report(self, message):
        requests.post(self.host, json=message)