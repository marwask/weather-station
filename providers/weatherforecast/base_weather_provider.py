from abc import abstractmethod
from datetime import datetime


class BaseWeatherProvider:

    def __init__(self):
        self.refresh()

    @abstractmethod
    def refresh(self):
        raise NotImplementedError

    @abstractmethod
    def _get_weather_condition_icon_map(self):
        raise NotImplementedError

    def get_weather_condition_icon(self, condition):
        try:
            return self._get_weather_condition_icon_map()[condition.lower()]
        except KeyError:
            print("expected icon condition: %s" % condition)
            return self._get_weather_condition_icon_map()["-"]

    def sunset(self):
        time = self.data.get('sunset', "-")
        return datetime.fromtimestamp(int(time))

    def sunrise(self):
        time = self.data.get('sunrise', "-")
        return datetime.fromtimestamp(int(time))

    def get_temp(self):
        return self.data.get('temp', "-")

    def get_min_temp(self):
        return self.data.get('temp_low', "-")

    def get_max_temp(self):
        return self.data.get('temp_high', "-")

    def get_humidity(self):
        return self.data.get('humidity', "-")

    def get_pressure(self):
        return self.data.get('pressure', "-")

    def get_current_condition(self):
        return self.data.get('condition', "-")

    def get_wind(self):
        # return self.data.get('wind_direction', "-") + " " + self.data.get('wind_speed', "")
        return self.data.get('wind_direction', "-")

    def get_icon_image(self):
        return self.current_icon

    def get_data(self):
        return self.data

    def get_forecasts(self):
        return self.data['forecasts']

    def get_sunrise(self):
        return self.data['sunrise']

    def get_sunset(self):
        return self.data['sunset']

    def _calc_low_temp(self, current_min, new):
        if current_min > new:
            return new
        return current_min

    def _calc_high_temp(self, current_max, new):
        if current_max < new:
            return new
        return current_max