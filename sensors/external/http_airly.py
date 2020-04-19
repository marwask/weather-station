import time
from sensors.sensor import Sensor
import requests
import json
from config.app import airly_installation_id, airly_api_key

class HttpAirly(Sensor):
    def __init__(self, mqtt_client):
        Sensor.__init__(self, mqtt_client)

    def run(self):
        while True:
            json_obj = self.get_data()
            for entry in json_obj['current']['values']:
                self.mqtt_client.publish("sensor_3/ext/" + entry['name'].lower(), round(entry['value'], 1))
            time.sleep(60)

    def get_data(self):
        session = requests.session()
        url = "https://airapi.airly.eu/v2/measurements/installation?indexType=AIRLY_CAQI&installationId=%s" % airly_installation_id
        response = session.get(url, headers={
            'Accept-Language': 'pl',
            'apikey': airly_api_key
        })
        json_obj = json.loads(response.text)
        session.close()
        return json_obj