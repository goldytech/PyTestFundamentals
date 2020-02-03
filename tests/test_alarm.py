from unittest.mock import Mock

from src.tyre_pressure.alarm import Alarm
from src.tyre_pressure.sensor import Sensor


def test_alarm_is_off_by_default():
    alarm = Alarm()
    assert not alarm.is_alarm_on


class StubSensor:
    def sample_pressure(self):
        return 15


def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor=StubSensor())
    alarm.check()
    assert alarm.is_alarm_on


def test_normal_pressure_alarm_stays_off():
    mock_sensor = Mock(Sensor)
    mock_sensor.sample_pressure.return_value = 18
    alarm = Alarm(mock_sensor)
    alarm.check()
    assert not alarm.is_alarm_on
