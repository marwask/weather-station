import time
from sensors.sensor import Sensor
try:
    from libs.adafruit_bme280 import BME280 as BME
except:
    pass

class BME280(Sensor):
    def __init__(self, mqtt_client):
        Sensor.__init__(self, mqtt_client)
        #self.sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
        self.sensor = BME()

    def run(self):
        while True:
            self.temperature = round(self.sensor.read_temperature(), 1)
            self.pressure = round(self.sensor.read_pressure() / 100, 0)
            self.humidity = round(self.sensor.read_humidity(), 0)
            self.mqtt_client.publish("sensor/base/temperature", self.temperature)
            self.mqtt_client.publish("sensor/base/pressure", self.pressure)
            self.mqtt_client.publish("sensor/base/humidity", self.humidity)
            time.sleep(10)