
class Measurement:

    def __init__(self, value, unit, round_value = 0):
        self.value = self.__get_foramtted_value(value, round_value)
        self.unit = unit

    def __get_foramtted_value(self, value, round_value):
        if value == None:
            return "-"
        elif round_value == 0:
            return str(int(round(value, round_value)))
        else:
            return str(round(value, round_value))