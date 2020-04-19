# from sensors.sensor import Sensor
# try:
#     import Adafruit_DHT
# except:
#     pass
#
# class DHT(Sensor):
#     def __init__(self, mqtt_client):
#         Sensor.__init__(self, mqtt_client)
#         self.sensor = ...
#
#     def refresh(self):
#         print("dht refresh")
#         try:
#             self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)
#         except Exception as e:
#             print(e)
#         self.mqtt_client.publish("sensor/base/humidity", self.humidity)
#         self.mqtt_client.publish("sensor/base/temperature", self.temperature)
#
#         print("dht published data: %s, %s" % (self.humidity, self.temperature))
#         print("dht published data2: %s, %s" % (self.get_temp(), self.get_humidity()))
#         print("after dht refresh")
