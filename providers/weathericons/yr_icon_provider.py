from providers.weathericons.base_weather_icon_provider import BaseWeatherIconProvider

class YrWeatherConditionIconProvider(BaseWeatherIconProvider):

    def __init__(self):
        super().__init__()
        self.path = "yr_icons/"
        self.day_suffix = "d"
        self.night_suffix = "n"

    def _icon_map(self):
        return {
            "-": { "icon" : "02.png", "night": True },
            "clear sky": { "icon" : "01.png", "night": True },
            "fair": { "icon" : "02.png", "night": True },
            "partly cloudy": { "icon" : "03.png", "night": True },
            "cloudy": { "icon" : "04.png" },
            "light rain showers": { "icon" : "40.png", "night": True },
            "rain showers": { "icon" : "05.png", "night": True },
            "heavy rain showers": { "icon" : "41.png", "night": True },
            "light rain showers and thunder": { "icon" : "24.png", "night": True },
            "rain showers and thunder": { "icon" : "06.png", "night": True },
            "heavy rain showers and thunder": { "icon" : "25.png", "night": True },
            "light sleet showers": { "icon" : "42.png", "night": True },
            "sleet showers": { "icon" : "07.png", "night": True },
            "heavy sleet showers": { "icon" : "43.png", "night": True },
            "lights sleet showers and thunder": { "icon" : "26.png", "night": True },
            "sleet showers and thunder": { "icon" : "20.png", "night": True },
            "heavy sleet showers and thunder": { "icon" : "27.png", "night": True },
            "light snow showers": { "icon" : "44.png", "night": True },
            "snow showers": { "icon" : "08.png", "night": True },
            "heavy snow showers": { "icon" : "45.png", "night": True },
            "lights snow showers and thunder": { "icon" : "28.png", "night": True },
            "snow showers and thunder": { "icon" : "21.png", "night": True },
            "heavy snow showers and thunder": { "icon" : "29.png", "night": True },
            "light rain": { "icon" : "46.png" },
            "rain": { "icon" : "09.png" },
            "heavy rain": { "icon" : "10.png" },
            "light rain and thunder": { "icon" : "30.png" },
            "rain and thunder": { "icon" : "22.png" },
            "heavy rain and thunder": { "icon" : "11.png" },
            "light sleet": { "icon" : "47.png" },
            "sleet": { "icon" : "12.png" },
            "heavy sleet": { "icon" : "48.png" },
            "light sleet and thunder": { "icon" : "31.png" },
            "sleet and thunder": { "icon" : "23.png" },
            "heavy sleet and thunder": { "icon" : "32.png" },
            "light snow": { "icon" : "49.png" },
            "snow": { "icon" : "13.png" },
            "heavy snow": { "icon" : "50.png" },
            "light snow and thunder": { "icon" : "33.png" },
            "snow and thunder": { "icon" : "14.png" },
            "heavy snow and thunder": { "icon" : "34.png" },
            "fog": { "icon" : "15.png" }
        }