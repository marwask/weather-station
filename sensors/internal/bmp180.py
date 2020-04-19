import time
from sensors.sensor import Sensor
import paho.mqtt.client as mqtt
try:
    import Adafruit_BMP.BMP085 as BMP085
except:
    pass

class BMP180(Sensor):
    def __init__(self, mqtt_client: mqtt.Client):
        Sensor.__init__(self, mqtt_client)
        self.sensor = BMP085.BMP085()

    def run(self):
        while True:
            self.temperature = round(self.sensor.read_temperature(), 1)
            self.pressure = round(self.sensor.read_pressure() / 100, 0)
            self.mqtt_client.publish("sensor/base/temperature2", self.temperature)
            self.mqtt_client.publish("sensor/base/pressure", self.pressure)
            time.sleep(8)