from config.mqtt_topics import Topic
from gui.measurement import Measurement
from providers.mqtt.mqtt_client import MqttClient


class MqttProvider():

    def __init__(self, mqtt_client: MqttClient):
        self.data = mqtt_client.get_topics_data()
        self.recent_loft_air = None

    def get_topic_value(self, topic: Topic):
        return self.data.get(topic[0], None)

    def get_living_room_temperature(self):
        return Measurement(self.get_topic_value(Topic.LIVING_ROOM_TEMPERATURE), "C", round_value=1)

    def get_living_room_humidity(self):
        return Measurement(self.get_topic_value(Topic.LIVING_ROOM_HUMIDITY), "%")

    def get_living_room_air(self):
        return Measurement(self.get_topic_value(Topic.LIVING_ROOM_AIR), "ppa")

    def get_living_room_pressure(self):
        return Measurement(self.get_topic_value(Topic.LIVING_ROOM_PRESSURE), "hpa", round_value=0)

    def get_attic_air(self):
        loft_air = self.get_topic_value(Topic.ATTIC_AIR)
        if loft_air != None and float(loft_air) > 4000:
            loft_air = self.recent_loft_air
        else:
            self.recent_loft_air = loft_air
        return Measurement(loft_air, "ppa")

    def get_attic_temperature(self):
        return Measurement(self.get_topic_value(Topic.ATTIC_TEMPERATURE), "C", round_value=1)

    def get_attic_humidity(self):
        return Measurement(self.get_topic_value(Topic.ATTIC_HUMIDITY), "%")

    def get_external_temperature(self):
        return Measurement(self.get_topic_value(Topic.EXTERNAL_DUST_TEMPERATURE), "C", round_value=1)

    def get_external_humidity(self):
        return Measurement(self.get_topic_value(Topic.EXTERNAL_DUST_HUMIDITY), "%")

    def get_external_dust_pm25(self):
        return Measurement(self.get_topic_value(Topic.EXTERNAL_DUST_PM25), "PM2.5")

    def get_external_dust_pm10(self):
        return Measurement(self.get_topic_value(Topic.EXTERNAL_DUST_PM10), "PM10")