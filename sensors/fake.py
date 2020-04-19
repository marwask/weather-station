import time

from sensors.sensor import Sensor


class Fake(Sensor):
    def __init__(self, mqtt_client):
        Sensor.__init__(self, mqtt_client)

    def run(self):
        while True:
            # print("fake")
            time.sleep(1)