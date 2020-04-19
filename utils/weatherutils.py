
def convert_hpa_to_inches(self, hpa):
    return hpa * 0.0295301

def convert_celsius_to_fahrenheit(self, temperature):
    return (temperature * 1.8) + 32.0

def calc_dew_point(self, temp, hum):
    x = 1 - 0.01 * hum
    dewpoint = (14.55 + 0.114 * temp) * x
    dewpoint = temp - dewpoint
    return int(self.convert_celsius_to_fahrenheit(dewpoint))