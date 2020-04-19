from sensors.sensor import Sensor
import time
try:
    import board
    import busio
    import adafruit_si7021
except:
    pass

class Si7021(Sensor):
    def __init__(self, mqtt_client):
        Sensor.__init__(self, mqtt_client)
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_si7021.SI7021(i2c)

    def run(self):
        while True:
            self.temperature = round(self.sensor.temperature, 1)
            self.humidity = round(self.sensor.relative_humidity, 1)
            self.mqtt_client.publish("sensor/base/temperature", self.temperature)
            self.mqtt_client.publish("sensor/base/humidity", self.humidity)
            print("after si7021 refresh")
            time.sleep(9)
