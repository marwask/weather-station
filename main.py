import sys
from time import sleep

import pygame

import config
from exporters.WeatherUndergroundExporter import WeatherUndergroundExporter
from gui.gui import Gui
from providers.mqtt.mqtt_provider import MqttClient
# from providers.weatherforecast.yahoo_weather_provider import YrWeatherProvider
# from providers.weatherforecast.test_weather_provider import TestWeatherProvider
from providers.weatherforecast.yr_weather_provider import WeatherForecastProvider
# from sensors.sparkfun_ccs811 import CCS811
# from sensors.dht import DHT
from sensors.internal.adafruit_ccs811 import CCS811
from sensors.internal.bmp180 import BMP180
from sensors.internal.si7021 import Si7021
from sensors.internal.bme280 import BME280
from sensors.fake import Fake
from sensors.external.http_airly import HttpAirly

####################################################################
FPS = 10

weather_forecast = WeatherForecastProvider('Polen/Masovia/Warszawa')
mqtt_client = MqttClient()

gui = Gui(weather_forecast, mqtt_client)
# gui.draw()
clock = pygame.time.Clock()

workers = [
    BMP180,
    Si7021,
    CCS811,
    BME280,
    Fake,
    WeatherUndergroundExporter,
    HttpAirly
]

for worker in workers:
    if getattr(config.app, worker.__name__) == True:
        instance = worker(mqtt_client)
        instance.start()

####################################################################


UPDATE_GUI_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_GUI_EVENT, 1000)
UPDATE_WEATHER_FORECAST_EVENT = UPDATE_GUI_EVENT + 1
pygame.time.set_timer(UPDATE_WEATHER_FORECAST_EVENT, 15 * 60 * 1000) # 15min

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == UPDATE_WEATHER_FORECAST_EVENT:
            weather_forecast.refresh()
    gui.draw()
    pygame.display.flip()

pygame.quit()