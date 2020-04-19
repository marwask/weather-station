import pygame

from config.app import LCD_WIDTH, LCD_HEIGHT
from gui.aligment import Aligment
from gui.measurement import Measurement


class GuiHelper():

    LABEL_FONT_COLOR = (254, 254, 50)
    FONT_COLOR = (224, 224, 224)
    TEMP_FONT_COLOR = (0x9d, 0xf6, 0x0a)
    HUMIDITY_FONT_COLOR = (0x00, 0xff, 0xcf)

    COLORS = [
        FONT_COLOR,
        TEMP_FONT_COLOR,
        HUMIDITY_FONT_COLOR
    ]

    def __init__(self, pygameutils):
        self.pygameutils = pygameutils
        self.surface = pygameutils.surface

    def draw_data_horizontal(self, x, y, place, measurements: []):
        self.draw_text(place, self.pygameutils.label_font, self.LABEL_FONT_COLOR, x, y)
        y = y + self.pygameutils.LABEL_FONT_SIZE * self.pygameutils.SCALE_HEIGHT
        if LCD_WIDTH > LCD_HEIGHT:
            margin = [0, 90, 150]
        else:
            margin = [0, 110, 200]
        for index, measurement in enumerate(measurements):
            self.draw_measurement(x + margin[index], y, self.COLORS[index], measurement)

    def draw_measurement(self, x, y, color, measurement: Measurement):
        value_label = self.draw_text(measurement.value, self.pygameutils.weather_font, color, x, y)
        self.draw_text(measurement.unit, self.pygameutils.unit_font, color, x + value_label.width * self.pygameutils.SCALE_WIDTH + 3, y + 2)

    def get_center(self, start_point, end_point):
        return start_point[0] - end_point[0], end_point[0] - start_point[0]

    def draw_image(self, path, x, y, width, height, scale=True):
        image = pygame.image.load(path)
        if scale:
            x = self.get_scaled_x(x)
            y = self.get_scaled_y(y)
            width = self.get_scaled_x(width)
            height = self.get_scaled_y(height)
        background_clock = pygame.transform.scale(image, [width, height])
        self.surface.blit(background_clock, (x, y))

    def draw_text(self, text, font, color, x, y, alignment=Aligment.LEFT, scaled=True):
        if not isinstance(text, str):
            text = str(text).encode("utf-8")
        value_label = font.render(text, True, color)
        if alignment == Aligment.RIGHT:
            text_width, text_height = font.size(text)
            x = x - text_width * self.pygameutils.SCALE_WIDTH
        if scaled:
            x = self.get_scaled_x(x)
            y = self.get_scaled_y(y)
        return self.surface.blit(value_label, (x, y))

    def get_center(self, length):
        return length / 2

    def draw_line(self, start_x, end_x, start_y, end_y):
        start_point = start_x, start_y
        end_point = end_x, end_y
        return self.draw_line(start_point, end_point)

    def draw_line(self, start_point, end_point):
        blue = 0, 0, 255
        pygame.draw.line(self.surface, blue, start_point, end_point)
        return start_point, end_point

    def draw_vertical_line(self, start_y, end_y):
        start_point = self.get_center(self.LCD_WIDTH), start_y
        end_point = self.get_center(self.LCD_WIDTH), end_y
        return self.draw_line(start_point, end_point)

    def draw_horizontal_line(self, start_x, end_x):
        start_point = start_x, self.get_center(self.LCD_HEIGHT)
        end_point = end_x, self.get_center(self.LCD_HEIGHT)
        return self.draw_line(start_point, end_point)

    def get_scaled_x(self, value):
        return int(value / self.pygameutils.SCALE_WIDTH)

    def get_scaled_y(self, value):
        return int(value / self.pygameutils.SCALE_HEIGHT)



