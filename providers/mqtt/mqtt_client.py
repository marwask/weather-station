import paho.mqtt.client as mqtt
from config.app import MQTT_CLIENT, MQTT_HOST, MQTT_PORT
from config.mqtt_topics import Topic


class MqttClient:

    def __init__(self):
        self.data = {}
        self.mqtt_client = mqtt.Client(MQTT_CLIENT, protocol=mqtt.MQTTv31, clean_session=False)
        print("connecting to broker")
        # self.mqtt_client.username_pw_set("", "")
        self.mqtt_client.connect(MQTT_HOST, port=MQTT_PORT)
        self._subscribe_topics()
        self.mqtt_client.on_message = self._on_message
        self.mqtt_client.on_disconnect = self._on_disconnect
        self.mqtt_client.loop_start()

    def get_mqtt_client(self):
        return self.mqtt_client

    def _subscribe_topics(self):
        for topic in Topic.get_topics():
            topic_name = topic[0]
            print("subscribing: " + topic_name)
            self.mqtt_client.subscribe(topic_name, qos=1)

    def _on_disconnect(self, client, userdata, rc):
        # # if rc != 0:
        # print("Unexpected MQTT disconnection. Will auto-reconnect: " + str(rc))
        # # self.mqtt_client.loop_stop()
        # # time.sleep(10)
        # # self.mqtt_client.loop_start()
        self.mqtt_client.reconnect()

    def _on_message(self, client, userdata, message):
        for topic in Topic.get_topics():
            topic_name = topic[0]
            if message.topic == topic_name:
                self.data[topic_name] = float(message.payload.decode('utf-8'))

    def get_topics_data(self):
        return self.data