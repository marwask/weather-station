import os
from datetime import datetime

import pytz

from config.app import HDMI, LCD_WIDTH, LCD_HEIGHT
from gui.aligment import Aligment
from gui.gui_helper import GuiHelper
from providers.mqtt.mqtt_client import MqttClient
from providers.mqtt.mqtt_provider import MqttProvider
from utils.pygameutils import PygameUtils

if HDMI == False:
    os.environ["SDL_FBDEV"] = "/dev/fb1"


class Gui():
    def __init__(self, weather_forecast_provider, mqtt_client: MqttClient):
        self.weather_provider = weather_forecast_provider
        self.mqtt_provider = MqttProvider(mqtt_client)
        self.pygameutils = PygameUtils()
        self.surface = self.pygameutils.surface
        self.gui_helper = GuiHelper(self.pygameutils)
        self.recent_loft_air = 0

    def draw(self):
        self._draw_background()
        self._draw_clock()
        self._draw_date()
        # self._draw_min_max_temp()
        self._draw_forecast()
        self._draw_sun_data()
        self._draw_sensors_data()

    def _draw_background(self):
        # https://www.psdgraphics.com/backgrounds/blue-ray-background/
        if LCD_WIDTH > LCD_HEIGHT:
            self.gui_helper.draw_image("resources/images/blue-ray-background.jpg", 0, 0, LCD_WIDTH, LCD_HEIGHT, scale=False)
            self.gui_helper.draw_image("resources/images/clock_background.png", 10, 10, 220, 300)
        else:
            self.gui_helper.draw_image("resources/images/blue-ray-background_blue.jpg", 0, 0, LCD_WIDTH, LCD_HEIGHT, scale=False)
            self.gui_helper.draw_image("resources/images/clock_background.png", 5, 5, 310, 230)

    def _draw_date(self):
        if LCD_WIDTH > LCD_HEIGHT: dimensions = (225, 168)
        else: dimensions = (180, 80)
        self.gui_helper.draw_text(self._current_date(), self.pygameutils.forecast_weather_font, self.gui_helper.FONT_COLOR, dimensions[0], dimensions[1], alignment=Aligment.RIGHT)

    def _draw_clock(self):
        if LCD_WIDTH > LCD_HEIGHT:
            xy = (27, 12)
            xywh = (60, 60, 115, 115)
        else:
            xy = (17, 12)
            xywh = (195, 10, 115, 115)
        self.gui_helper.draw_text(self._current_time(), self.pygameutils.clock_font, self.gui_helper.FONT_COLOR, xy[0], xy[1])
        self.gui_helper.draw_image(self.weather_provider.get_weather_condition_icon(self.weather_provider.get_current_condition()), xywh[0], xywh[1], xywh[2], xywh[3])

    def _draw_min_max_temp(self):
        x = 17
        self.gui_helper.draw_text("max", self.pygameutils.label_font, self.gui_helper.LABEL_FONT_COLOR, x, 120)
        value = self.gui_helper.draw_text(self.weather_provider.get_max_temp(), self.pygameutils.forecast_weather_font, self.gui_helper.FONT_COLOR, x, 132)
        self.gui_helper.draw_text("C", self.pygameutils.unit_font, self.gui_helper.FONT_COLOR, x + 2 + value.width * self.pygameutils.SCALE_WIDTH, 132)

        self.gui_helper.draw_text("min", self.pygameutils.label_font, self.gui_helper.LABEL_FONT_COLOR, x, 156)
        value = self.gui_helper.draw_text(self.weather_provider.get_min_temp(), self.pygameutils.forecast_weather_font, self.gui_helper.FONT_COLOR, x, 168)
        self.gui_helper.draw_text("C", self.pygameutils.unit_font, self.gui_helper.FONT_COLOR, x + 2 + value.width * self.pygameutils.SCALE_WIDTH, 168)

        self.gui_helper.draw_text("wind", self.pygameutils.label_font, self.gui_helper.LABEL_FONT_COLOR, 225, 120, alignment=Aligment.RIGHT)
        self.gui_helper.draw_text(self.weather_provider.get_wind(), self.pygameutils.forecast_weather_font, self.gui_helper.FONT_COLOR, 225, 132, alignment=Aligment.RIGHT)

    def _draw_forecast(self):
        if LCD_WIDTH > LCD_HEIGHT: base_margin = 55
        else: base_margin = 80
        margin = 0
        for forecast in self.weather_provider.get_forecasts()[1:5]:
            day = forecast['day']
            temp_high = forecast['temp_high']
            temp_low = forecast['temp_low']
            condition = forecast['condition']
            self._draw_forecast_entry(margin, day, self.weather_provider.get_weather_condition_icon(condition), temp_low, temp_high)
            margin += base_margin

    def _draw_forecast_entry(self, x, day, icon, temp_min, temp_max):
        if LCD_WIDTH > LCD_HEIGHT:
            self.gui_helper.draw_text(day, self.pygameutils.label_font, self.gui_helper.LABEL_FONT_COLOR, x + 31, 200)
            self.gui_helper.draw_image(icon, x + 17, 215, 40, 40)
            self.gui_helper.draw_text(temp_max, self.pygameutils.forecast_weather_font, self.gui_helper.FONT_COLOR, x + 17, 255)
            self.gui_helper.draw_text("/" + str(temp_min), self.pygameutils.unit_font, self.gui_helper.FONT_COLOR, x + 40, 260)
        else:
            self.gui_helper.draw_text(day, self.pygameutils.label_font, self.gui_helper.LABEL_FONT_COLOR, x + 55, 150)
            self.gui_helper.draw_image(icon, x + 17, 155, 40, 40)
            self.gui_helper.draw_text(temp_max, self.pygameutils.forecast_weather_font, self.gui_helper.FONT_COLOR, x + 17, 193)
            self.gui_helper.draw_text("/" + str(temp_min), self.pygameutils.unit_font, self.gui_helper.FONT_COLOR, x + 40, 198)

    def _draw_sun_data(self):
        if LCD_WIDTH > LCD_HEIGHT:
            self.gui_helper.draw_text(self.weather_provider.get_sunrise(), self.pygameutils.unit_font, self.gui_helper.FONT_COLOR, 20, 291)
            self.gui_helper.draw_text(self.weather_provider.get_sunset(), self.pygameutils.unit_font, self.gui_helper.FONT_COLOR, 185, 291)
        else:
            self.gui_helper.draw_text(self.weather_provider.get_sunrise(), self.pygameutils.unit_font, self.gui_helper.FONT_COLOR, 20, 220)
            self.gui_helper.draw_text(self.weather_provider.get_sunset(), self.pygameutils.unit_font, self.gui_helper.FONT_COLOR, 260, 220)

    def _draw_sensors_data(self):
        if LCD_WIDTH > LCD_HEIGHT:
            x = 240
            y = 0
            margin = [10, 70, 130, 190]
        else:
            x = 15
            y = 235
            margin = [10, 70, 130, 190]

        measurements = [
            self.mqtt_provider.get_living_room_temperature(),
            self.mqtt_provider.get_living_room_humidity(),
            self.mqtt_provider.get_living_room_air()
        ]
        self.gui_helper.draw_data_horizontal(x, y + margin[0], "living room", measurements)

        measurements = [
            self.mqtt_provider.get_attic_temperature(),
            self.mqtt_provider.get_attic_humidity(),
            self.mqtt_provider.get_attic_air()
        ]
        self.gui_helper.draw_data_horizontal(x, y + margin[1], "attic", measurements)

        measurements = [
            self.mqtt_provider.get_external_temperature(),
            self.mqtt_provider.get_external_humidity(),
            self.mqtt_provider.get_living_room_pressure()
        ]
        self.gui_helper.draw_data_horizontal(x, y + margin[2], "outside", measurements)

        measurements = [
            self.mqtt_provider.get_external_dust_pm25(),
            self.mqtt_provider.get_external_dust_pm10()
        ]
        self.gui_helper.draw_data_horizontal(x, y + margin[3], "dust", measurements)

    def _current_time(self):
        now = datetime.now(pytz.timezone('Europe/Warsaw'))
        pattern = "{:02d}:{:02d}"
        return pattern.format(now.hour, now.minute)

    def _current_date(self):
        now = datetime.now(pytz.timezone('Europe/Warsaw'))
        return now.strftime("%Y-%m-%d")