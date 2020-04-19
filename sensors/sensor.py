#!/usr/bin/python

import threading
from providers.mqtt.mqtt_provider import MqttClient

class Sensor(threading.Thread):

    def __init__(self, mqttclient: MqttClient):
        threading.Thread.__init__(self)
        self.mqtt_client = mqttclient.get_mqtt_client()
        self.data = {}