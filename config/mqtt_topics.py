
class Topic():
    EXTERNAL_TEMPERATURE = 'sensor_3/ext/temperature',
    EXTERNAL_HUMIDITY = 'sensor_3/ext/humidity',
    EXTERNAL_DUST_PM25 = 'hooks/devices/0/SensorData/PM2.5',
    EXTERNAL_DUST_PM10 = 'hooks/devices/0/SensorData/PM10',
    EXTERNAL_DUST_TEMPERATURE = 'hooks/devices/0/SensorData/Temperature',
    EXTERNAL_DUST_HUMIDITY = 'hooks/devices/0/SensorData/Humidity',

    ATTIC_TEMPERATURE = 'sensor_2/loft/temperature',
    ATTIC_HUMIDITY = 'sensor_2/loft/humidity',
    ATTIC_AIR = 'sensor_2/loft/air',

    LIVING_ROOM_TEMPERATURE = 'sensor/base/temperature',
    # LIVING_ROOM_TEMPERATURE = 'sensor/base/temperature2',
    LIVING_ROOM_HUMIDITY = 'sensor/base/humidity',
    LIVING_ROOM_AIR = 'sensor/base/air',
    LIVING_ROOM_PRESSURE = 'sensor/base/pressure',

    TEST = 'test'

    @staticmethod
    def get_topics():
        return [
            Topic.ATTIC_AIR,
            Topic.ATTIC_HUMIDITY,
            Topic.ATTIC_TEMPERATURE,
            Topic.LIVING_ROOM_AIR,
            Topic.LIVING_ROOM_HUMIDITY,
            Topic.LIVING_ROOM_TEMPERATURE,
            Topic.LIVING_ROOM_PRESSURE,
            Topic.EXTERNAL_HUMIDITY,
            Topic.EXTERNAL_TEMPERATURE,
            Topic.EXTERNAL_DUST_HUMIDITY,
            Topic.EXTERNAL_DUST_TEMPERATURE,
            Topic.EXTERNAL_DUST_PM25,
            Topic.EXTERNAL_DUST_PM10
        ]