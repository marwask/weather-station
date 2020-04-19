import time
from sensors.sensor import Sensor
try:
    from libs.sparkfun_ccs811 import CCS811 as ccs
except:
    pass

class CCS811(Sensor):
    def __init__(self, mqtt_client):
        Sensor.__init__(self, mqtt_client)
        self.sensor = ccs()
        self.sensor.setup()

    def run(self):
        while True:
            print("ccs811 refresh")
            self.sensor.get_base_line()
            if self.sensor.data_available():
                self.sensor.read_logorithm_results()
                self.air = self.sensor.CO2
                if self.air < 5000:
                    self.mqtt_client.publish("sensor/base/air", self.air)
            # elif self.sensor.check_for_error():
            #     self.sensor.print_error()
            print("after ccs811 refresh")
            time.sleep(20)