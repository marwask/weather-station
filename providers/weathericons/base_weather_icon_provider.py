
class BaseWeatherIconProvider():

    def __init__(self):
        self.BASE_ICON_PATH = "resources/images/"
        self.day_prefix = ""
        self.night_prefix = ""
        self.day_suffix = ""
        self.night_suffix = ""

    def get_weather_icon_map(self, night=False):
        icon_map = self._icon_map()
        for key, value in icon_map.items():
            icon = value['icon']
            try:
                if night == False and value['night']:
                    icon = self.day_prefix + icon[:-4] + self.day_suffix + icon[-4:]
                elif night == True and value['night']:
                    icon = self.night_prefix + icon[:-4] + self.night_suffix + icon[-4:]
            except KeyError:
                pass
            icon_map[key] = self.BASE_ICON_PATH + self.path + icon
        return icon_map