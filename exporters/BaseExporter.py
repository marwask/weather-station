from abc import abstractmethod

import requests
import threading
import time

class BaseExporter(threading.Thread):

    def __init__(self, mqtt_client):
        threading.Thread.__init__(self)
        self.data = mqtt_client.get_data()

    def invoke_get_request(self, url, params):
        response = requests.get(url=url, params=params)
        # data = response.json()
        # print("response: " + data)

    @abstractmethod
    def export(self, data):
        raise NotImplementedError("Not implemented...")

    def run(self):
        while True:
            self.export(self.data)
            time.sleep(60)