from abc import abstractmethod

from providers.weatherforecast.base_weather_provider import BaseWeatherProvider
from providers.weathericons.yr_icon_provider import YrWeatherConditionIconProvider


class WeatherForecastProvider(BaseWeatherProvider):

    def __init__(self, location):
        self.location = location
        super().__init__()

    def _get_weather_condition_icon_map(self):
        return YrWeatherConditionIconProvider().get_weather_icon_map()

    def refresh(self):
        try:
            self.data = {
                'temp': 23.7,
                # 'condition': "Sunny",
                # 'condition': "Cloudy",
                'condition': "clear sky",
                'wind_direction': "NE",
                'pressure': 1002,
                'humidity': 53.2,
                'sunrise': "07:25",
                'sunset': "15:51",
                'forecasts': {}
            }

            forecasts_array = []
            for i in range(5):
                forecast_entry = {
                    'day': "TMP",
                    'temp_high': 25,
                    'temp_low': 14,
                    'condition': "Cloudy"
                }
                forecasts_array.append(forecast_entry)
            self.data['forecasts'] = forecasts_array

            forecast = forecasts_array[0]
            self.data['temp_high'] = forecast['temp_high']
            self.data['temp_low'] = forecast['temp_low']
        except Exception as e:
            print(e)
