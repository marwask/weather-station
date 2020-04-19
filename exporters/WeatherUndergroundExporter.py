from exporters.BaseExporter import BaseExporter
from config.mqtt_topics import Topic
from utils.weatherutils import calc_dew_point, convert_celsius_to_fahrenheit, convert_hpa_to_inches
from config.app import weatherunderground_url, weatherunderground_id, weatherunderground_password


class WeatherUndergroundExporter(BaseExporter):

    def __init__(self, mqtt_client):
        BaseExporter.__init__(self, mqtt_client)

    def export(self, data):
        try:
            pressure = Topic.LIVING_ROOM_PRESSURE
            humidity = Topic.EXTERNAL_HUMIDITY
            temp = Topic.EXTERNAL_TEMPERATURE

            if pressure > 969 and pressure < 1039:
                params = {
                    'ID': weatherunderground_id,
                    'PASSWORD': weatherunderground_password,
                    'dateutc': 'now',
                    'baromin': '' + str(convert_hpa_to_inches(pressure)) + '',
                    'tempf': '' + str(convert_celsius_to_fahrenheit(temp)) + '',
                    'dewptf': '' + str(calc_dew_point(temp, humidity)) + '',
                    'humidity': '' + str(humidity) + '',
                    'action': 'updateraw'
                }
                self.invoke_get_request(weatherunderground_url, params)
        except KeyError as e:
            print("key error: " + str(e))


