import time
from sensors.sensor import Sensor
try:
    import adafruit_ccs811
    import board
    import busio
except:
    pass

class CCS811(Sensor):
    def __init__(self, mqtt_client):
        Sensor.__init__(self, mqtt_client)
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_ccs811.CCS811(i2c, address=0x5B)

    def run(self):
        while True:
            print("ccs811 refresh")
            # self.temperature = round(self.sensor.temperature, 1)
            self.air = self.sensor.eco2
            if self.air < 5000:
                # self.mqtt_client.publish("sensor/base/temperature3", self.temperature)
                self.mqtt_client.publish("sensor/base/air", self.air)
            print("after ccs811 refresh")
            time.sleep(1)