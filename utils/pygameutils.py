import pygame
import os
from config.app import LCD_WIDTH, LCD_HEIGHT, HDMI


class PygameUtils:

    LCD_BASE_WIDTH = 480
    LCD_BASE_HEIGHT = 320

    if LCD_WIDTH > LCD_HEIGHT:
        SCALE_WIDTH = LCD_BASE_WIDTH / LCD_WIDTH
    else:
        SCALE_WIDTH = LCD_BASE_HEIGHT / LCD_WIDTH

    if LCD_WIDTH > LCD_HEIGHT:
        SCALE_HEIGHT = LCD_BASE_HEIGHT / LCD_HEIGHT
    else:
        SCALE_HEIGHT = LCD_BASE_WIDTH / LCD_HEIGHT

    CLOCK_FONT_SIZE = 80
    LABEL_FONT_SIZE = 12
    VALUE_FONT_SIZE = 35
    UNIT_FONT_SIZE = 15
    FORECAST_VALUE_FONT_SIZE = 22

    CLOCK_FONT_SIZE = int(CLOCK_FONT_SIZE / SCALE_WIDTH)
    LABEL_FONT_SIZE = int(LABEL_FONT_SIZE / SCALE_WIDTH)
    VALUE_FONT_SIZE = int(VALUE_FONT_SIZE / SCALE_WIDTH)
    FORECAST_VALUE_FONT_SIZE = int(FORECAST_VALUE_FONT_SIZE / SCALE_WIDTH)
    UNIT_FONT_SIZE = int(UNIT_FONT_SIZE / SCALE_WIDTH)
    # CLOCK_FONT_SIZE = int(CLOCK_FONT_SIZE / SCALE_HEIGHT)
    # LABEL_FONT_SIZE = int(LABEL_FONT_SIZE / SCALE_HEIGHT)
    # VALUE_FONT_SIZE = int(VALUE_FONT_SIZE / SCALE_HEIGHT)
    # FORECAST_VALUE_FONT_SIZE = int(FORECAST_VALUE_FONT_SIZE / SCALE_HEIGHT)
    # UNIT_FONT_SIZE = int(UNIT_FONT_SIZE / SCALE_HEIGHT)

    ###################

    def __init__(self):
        self.surface = None
        self.clock_font = None
        self.weather_font = None
        self.forecast_weather_font = None
        self.label_font = None
        self.unit_font = None
        self.init_pygame()
        self.init_fonts()

    def init_pygame(self):
        if HDMI == True:
            disp_no = os.getenv("DISPLAY")
            if disp_no:
                print("I'm running under X display = {0}".format(disp_no))
            drivers = ['X11', 'fbcon', 'directfb', 'svgalib']
            found = False
            for driver in drivers:
                if not os.getenv('SDL_VIDEODRIVER'):
                    os.putenv('SDL_VIDEODRIVER', driver)
                try:
                    pygame.display.init()
                except pygame.error:
                    print('Driver: {0} failed.'.format(driver))
                    continue
                found = True
                break

            if not found:
                raise Exception('No suitable video driver found!')

            # size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
            # print ("Framebuffer size: %d x %d" % (size[0], size[1]))
            # self.surface = pygame.display.set_mode(size, pygame.FULLSCREEN)
            self.surface = pygame.display.set_mode((LCD_WIDTH, LCD_HEIGHT), pygame.FULLSCREEN)
            # self.surface.fill((0, 0, 0))
            # pygame.font.init()
            # pygame.display.update()
        else:
            pygame.display.init()
            pygame.mouse.set_visible(False)
            self.surface = pygame.display.set_mode((LCD_WIDTH, LCD_HEIGHT), 0, 32)

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print("Framebuffer size: %d x %d" % (size[0], size[1]))
        self.surface.fill((0, 0, 0))
        pygame.font.init()
        pygame.display.update()

    def init_fonts(self):
        self.clock_font = pygame.font.Font("resources/fonts/digital-mono.ttf", self.CLOCK_FONT_SIZE)
        self.weather_font = pygame.font.Font("resources/fonts/digital-mono.ttf", self.VALUE_FONT_SIZE)
        self.forecast_weather_font = pygame.font.Font("resources/fonts/digital-mono.ttf", self.FORECAST_VALUE_FONT_SIZE)
        self.label_font = pygame.font.Font("resources/fonts/digital-mono.ttf", self.LABEL_FONT_SIZE)
        self.unit_font = pygame.font.Font("resources/fonts/digital-mono.ttf", self.UNIT_FONT_SIZE)

    # def get_scaled_x(self, value):
    #     return int(value / self.SCALE_WIDTH)
    #
    # def get_scaled_y(self, value):
    #     return int(value / self.SCALE_HEIGHT)