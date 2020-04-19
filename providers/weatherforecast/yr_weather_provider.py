from abc import abstractmethod

from yr.libyr import Yr
from dateutil import parser
from providers.weathericons.yr_icon_provider import YrWeatherConditionIconProvider
from providers.weatherforecast.base_weather_provider import BaseWeatherProvider


class WeatherForecastProvider(BaseWeatherProvider):

    def __init__(self, location):
        self.location = location
        super().__init__()

    def _get_weather_condition_icon_map(self):
        return YrWeatherConditionIconProvider().get_weather_icon_map()

    def refresh(self):
        try:
            # http://fil.nrk.no/yr/viktigestader/verda.txt
            weather = Yr(location_name=self.location)
            now = weather.now()
            weatherdata = weather.dictionary['weatherdata']

            self.data = {
                'temp': now['temperature']['@value'],
                'condition': now['symbol']['@name'],
                'pressure': now['pressure']['@value'],
                'humidity': "-",
                'wind_direction': now['windDirection']['@code'],
                'wind_speed': now['windSpeed']['@mps'],
                'sunrise': weatherdata['sun']['@rise'][11:-3],
                'sunset': weatherdata['sun']['@set'][11:-3],
                'forecasts': {}
            }

            forecasts = weatherdata['forecast']['tabular']['time']
            forecasts_array = []

            condition = None
            temp_high = -99
            temp_low = 99
            for forecast in forecasts:
                condition = forecast['symbol']['@name']
                temp = int(forecast['temperature']['@value'])
                temp_low = self._calc_low_temp(temp_low, temp)
                temp_high = self._calc_high_temp(temp_high, temp)
                if forecast['@period'] == "3":
                    forecast_entry = {
                        'day': self.get_day_of_week(forecast['@from']),
                        'temp_high': temp_high,
                        'temp_low': temp_low,
                        'condition': condition
                    }
                    temp_high = -99
                    temp_low = 99
                    forecasts_array.append(forecast_entry)
            self.data['forecasts'] = forecasts_array

            forecast = forecasts_array[0]
            self.data['temp_high'] = forecast['temp_high']
            self.data['temp_low'] = forecast['temp_low']
        except Exception as e:
            print(e)

    def get_day_of_week(self, date):
        # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # dayNumber = date.weekday()
        # return days[dayNumber]
        return parser.parse(date).strftime("%a")