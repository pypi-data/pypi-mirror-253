"""Holds the Data Calsses for WeatherFlow Forecast Wrapper."""

from __future__ import annotations
from datetime import datetime
import math
import logging
_LOGGER = logging.getLogger(__name__)

class WeatherFlowForecastData:
    """Class to hold forecast data."""

        # pylint: disable=R0913, R0902, R0914
    def __init__(
        self,
        datetime: datetime,
        timestamp: int,
        apparent_temperature: float,
        condition: str,
        dew_point: float,
        humidity: int,
        icon: str,
        precipitation: float,
        pressure: float,
        temperature: float,
        uv_index: int,
        wind_bearing: int,
        wind_gust_speed: float,
        wind_speed: float,
        forecast_daily: WeatherFlowForecastDaily = None,
        forecast_hourly: WeatherFlowForecastHourly = None,
    ) -> None:
        """Dataset constructor."""
        self._datetime = datetime
        self._timestamp = timestamp
        self._apparent_temperature = apparent_temperature
        self._condition = condition
        self._dew_point = dew_point
        self._humidity = humidity
        self._icon = icon
        self._precipitation = precipitation
        self._pressure = pressure
        self._temperature = temperature
        self._uv_index = uv_index
        self._wind_bearing = wind_bearing
        self._wind_gust_speed = wind_gust_speed
        self._wind_speed = wind_speed
        self._forecast_daily = forecast_daily
        self._forecast_hourly = forecast_hourly


    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)."""
        return self._temperature

    @property
    def dew_point(self) -> float:
        """Dew Point (Celcius)."""
        return self._dew_point

    @property
    def condition(self) -> str:
        """Weather condition text."""
        return self._condition

    @property
    def icon(self) -> str:
        """Weather condition symbol."""
        return self._icon

    @property
    def humidity(self) -> int:
        """Humidity (%)."""
        return self._humidity

    @property
    def apparent_temperature(self) -> float:
        """Feels like temperature (Celcius)."""
        return self._apparent_temperature

    @property
    def precipitation(self) -> float:
        """Precipitation (mm)."""
        return self._precipitation

    @property
    def pressure(self) -> float:
        """Sea Level Pressure (MB)."""
        return self._pressure

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)."""
        return self._wind_bearing

    @property
    def wind_gust_speed(self) -> float:
        """Wind gust (m/s)."""
        return self._wind_gust_speed

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)."""
        return self._wind_speed

    @property
    def uv_index(self) -> float:
        """UV Index."""
        return self._uv_index

    @property
    def datetime(self) -> datetime:
        """Valid time."""
        return self._datetime

    @property
    def datetimestamptime(self) -> int:
        """Timestamp."""
        return self._timestamp

    @property
    def forecast_daily(self) -> WeatherFlowForecastDaily:
        """Forecast List."""
        return self._forecast_daily

    @forecast_daily.setter
    def forecast_daily(self, new_forecast):
        """Forecast daily new value."""
        self._forecast_daily = new_forecast

    @property
    def forecast_hourly(self) -> WeatherFlowForecastHourly:
        """Forecast List."""
        return self._forecast_hourly

    @forecast_hourly.setter
    def forecast_hourly(self, new_forecast):
        """Forecast hourly new value."""
        self._forecast_hourly = new_forecast

class WeatherFlowForecastDaily:
    """Class to hold daily forecast data."""

        # pylint: disable=R0913, R0902, R0914
    def __init__(
        self,
        datetime: datetime,
        timestamp: int,
        temperature: float,
        temp_low: float,
        condition: str,
        icon: str,
        precipitation_probability: int,
        precipitation: float,
        wind_bearing: int,
        wind_speed: float,
        wind_gust: float,
    ) -> None:
        """Dataset constructor."""
        self._datetime = datetime
        self._timestamp = timestamp
        self._temperature = temperature
        self._temp_low = temp_low
        self._condition = condition
        self._icon = icon
        self._precipitation_probability = precipitation_probability
        self._precipitation = precipitation
        self._wind_bearing = wind_bearing
        self._wind_speed = wind_speed
        self._wind_gust = wind_gust

    @property
    def datetime(self) -> datetime:
        """Valid time."""
        return self._datetime

    @property
    def timestamp(self) -> int:
        """Timestamp."""
        return self._timestamp

    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)."""
        return self._temperature

    @property
    def temp_low(self) -> float:
        """Air temperature min during the day (Celcius)."""
        return self._temp_low

    @property
    def condition(self) -> str:
        """Weather condition text."""
        return self._condition

    @property
    def icon(self) -> str:
        """Weather condition symbol."""
        return self._icon

    @property
    def precipitation_probability (self) -> int:
        """Posobility of Precipiation (%)."""
        return self._precipitation_probability

    @property
    def precipitation(self) -> float:
        """Precipitation (mm)."""
        return self._precipitation

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)."""
        return self._wind_bearing

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)."""
        return self._wind_speed

    @property
    def wind_gust(self) -> float:
        """Wind gust (m/s)."""
        return self._wind_gust

class WeatherFlowForecastHourly:
    """Class to hold hourly forecast data."""

        # pylint: disable=R0913, R0902, R0914
    def __init__(
        self,
        datetime: datetime,
        timestamp: int,
        temperature: float,
        apparent_temperature: float,
        condition: str,
        icon: str,
        humidity: int,
        precipitation: float,
        precipitation_probability: int,
        pressure: float,
        wind_bearing: float,
        wind_gust_speed: int,
        wind_speed: int,
        uv_index: float,
    ) -> None:
        """Dataset constructor."""
        self._datetime = datetime
        self._timestamp = timestamp
        self._temperature = temperature
        self._apparent_temperature = apparent_temperature
        self._condition = condition
        self._icon = icon
        self._humidity = humidity
        self._precipitation = precipitation
        self._precipitation_probability = precipitation_probability
        self._pressure = pressure
        self._wind_bearing = wind_bearing
        self._wind_gust_speed = wind_gust_speed
        self._wind_speed = wind_speed
        self._uv_index = uv_index

    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)."""
        return self._temperature

    @property
    def condition(self) -> str:
        """Weather condition text."""
        return self._condition

    @property
    def icon(self) -> str:
        """Weather condition symbol."""
        return self._icon

    @property
    def humidity(self) -> int:
        """Humidity (%)."""
        return self._humidity

    @property
    def apparent_temperature(self) -> float:
        """Feels like temperature (Celcius)."""
        return self._apparent_temperature

    @property
    def precipitation(self) -> float:
        """Precipitation (mm)."""
        return self._precipitation

    @property
    def precipitation_probability (self) -> int:
        """Posobility of Precipiation (%)."""
        return self._precipitation_probability

    @property
    def pressure(self) -> float:
        """Sea Level Pressure (MB)."""
        return self._pressure

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)."""
        return self._wind_bearing

    @property
    def wind_gust_speed(self) -> float:
        """Wind gust (m/s)."""
        return self._wind_gust_speed

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)."""
        return self._wind_speed

    @property
    def uv_index(self) -> float:
        """UV Index."""
        return self._uv_index

    @property
    def datetime(self) -> datetime:
        """Valid time."""
        return self._datetime

    @property
    def timestamp(self) -> int:
        """Timestamp."""
        return self._timestamp


class WeatherFlowDeviceData:
    """Class to hold device data."""

        # pylint: disable=R0913, R0902, R0914
    def __init__(
            self,
            device_id: int,
            voltage: float,
            precipitation_type: int,
    ) -> None:
        """Dataset constructor."""
        self._device_id = device_id
        self._voltage = voltage
        self._precipitation_type = precipitation_type

    @property
    def device_id(self) -> int:
        """Return device id."""
        return self._device_id

    @property
    def voltage(self) -> float:
        """Return voltage of device."""
        return self._voltage

    @property
    def precipitation_type(self) -> int:
        """Return Precipiation type."""
        return self._precipitation_type

    @property
    def battery(self) -> int:
        """Battery (%)."""
        if self._voltage is None:
            return None

        if self._voltage > 2.80:
            _percent = 100
        elif self._voltage < 1.80:
            _percent = 0
        else:
            _percent = (self._voltage - 1.8) * 100

        return _percent

class WeatherFlowStationData:
    """Class to hold station data."""

        # pylint: disable=R0913, R0902, R0914
    def __init__(
            self,
            station_name: str,
            latitude: float,
            longitude: float,
            timezone: str,
            device_id: int,
            firmware_revision: str,
            serial_number: str,
    ) -> None:
        """Dataset constructor."""
        self._station_name = station_name
        self._latitude = latitude
        self._longitude = longitude
        self._timezone = timezone
        self._device_id = device_id
        self._firmware_revision = firmware_revision
        self._serial_number = serial_number

    @property
    def station_name(self) -> str:
        """Name of the Station."""
        return self._station_name

    @property
    def latitude(self) -> float:
        """Latitude of station."""
        return self._latitude

    @property
    def longitude(self) -> float:
        """Longitude of station."""
        return self._longitude

    @property
    def timezone(self) -> str:
        """Timezone of station."""
        return self._timezone

    @property
    def device_id(self) -> int:
        """Device ID."""
        return self._device_id

    @property
    def firmware_revision(self) -> str:
        """Firmware Version."""
        return self._firmware_revision

    @property
    def serial_number(self) -> str:
        """Device Serial Number."""
        return self._serial_number

class WeatherFlowSensorData:
    """Class to hold sensor data."""

        # pylint: disable=R0913, R0902, R0914
    def __init__(
            self,
            data_available: bool,
            air_density: float,
            air_temperature: float,
            barometric_pressure: float,
            brightness: int,
            delta_t: float,
            dew_point: float,
            feels_like: float,
            heat_index: float,
            lightning_strike_count: int,
            lightning_strike_count_last_1hr: int,
            lightning_strike_count_last_3hr: int,
            lightning_strike_last_distance: int,
            lightning_strike_last_epoch: int,
            precip: float,
            precip_accum_last_1hr: float,
            precip_accum_local_day: float,
            precip_accum_local_yesterday: float,
            precip_minutes_local_day: int,
            precip_minutes_local_yesterday: int,
            precipitation_type: int,
            pressure_trend: str,
            relative_humidity: int,
            sea_level_pressure: float,
            solar_radiation: float,
            station_pressure: float,
            timestamp: int,
            uv: float,
            voltage: float,
            wet_bulb_globe_temperature: float,
            wet_bulb_temperature: float,
            wind_avg: float,
            wind_chill: float,
            wind_direction: int,
            wind_gust: float,
            wind_lull: float,
            precip_accum_local_day_final: float,
            precip_accum_local_yesterday_final: float,
            precip_minutes_local_day_final: int,
            precip_minutes_local_yesterday_final: int,
            elevation: float,
            station_name: str,
    ) -> None:
        """Dataset constructor."""
        self._data_available = data_available
        self._air_density = air_density
        self._air_temperature = air_temperature
        self._barometric_pressure = barometric_pressure
        self._brightness = brightness
        self._delta_t = delta_t
        self._dew_point = dew_point
        self._feels_like = feels_like
        self._heat_index = heat_index
        self._lightning_strike_count = lightning_strike_count
        self._lightning_strike_count_last_1hr = lightning_strike_count_last_1hr
        self._lightning_strike_count_last_3hr = lightning_strike_count_last_3hr
        self._lightning_strike_last_distance = lightning_strike_last_distance
        self._lightning_strike_last_epoch = lightning_strike_last_epoch
        self._precip = precip
        self._precip_accum_last_1hr = precip_accum_last_1hr
        self._precip_accum_local_day = precip_accum_local_day
        self._precip_accum_local_yesterday = precip_accum_local_yesterday
        self._precip_minutes_local_day = precip_minutes_local_day
        self._precip_minutes_local_yesterday = precip_minutes_local_yesterday
        self._precipitation_type = precipitation_type
        self._pressure_trend = pressure_trend
        self._relative_humidity = relative_humidity
        self._sea_level_pressure = sea_level_pressure
        self._solar_radiation = solar_radiation
        self._station_pressure = station_pressure
        self._timestamp = timestamp
        self._uv = uv
        self._voltage = voltage
        self._wet_bulb_globe_temperature = wet_bulb_globe_temperature
        self._wet_bulb_temperature = wet_bulb_temperature
        self._wind_avg = wind_avg
        self._wind_chill = wind_chill
        self._wind_direction = wind_direction
        self._wind_gust = wind_gust
        self._wind_lull = wind_lull
        self._precip_accum_local_day_final = precip_accum_local_day_final
        self._precip_accum_local_yesterday_final = precip_accum_local_yesterday_final
        self._precip_minutes_local_day_final = precip_minutes_local_day_final
        self._precip_minutes_local_yesterday_final = precip_minutes_local_yesterday_final
        self._elevation = elevation
        self._station_name = station_name

    @property
    def data_available(self) -> bool:
        """Return if sensor data is available."""
        return self._data_available

    @property
    def absolute_humidity(self) -> float:
        """Aboslute Humidity (g.m-3)."""
        if self._air_temperature is None or self._relative_humidity is None:
            return None

        kelvin = self._air_temperature + 273.16
        humidity = self._relative_humidity / 100
        return (1320.65 / kelvin) * humidity * (10 ** ((7.4475 * (kelvin - 273.14)) / (kelvin - 39.44)))

    @property
    def air_density(self) -> float:
        """Air Density."""
        return self._air_density

    @property
    def air_temperature(self) -> float:
        """Outside Temperature."""
        return self._air_temperature

    @property
    def barometric_pressure(self) -> float:
        """Barometric Pressure."""
        return self._barometric_pressure

    @property
    def battery(self) -> int:
        """Battery (%)."""
        if self._voltage is None:
            return None

        if self._voltage > 2.80:
            _percent = 100
        elif self._voltage < 1.80:
            _percent = 0
        else:
            _percent = (self._voltage - 1.8) * 100

        return _percent

    @property
    def beaufort(self) -> int:
        """Beaufort Value."""
        if self._wind_avg is None:
            return None

        mapping_text = {
            "32.7": 12,
            "28.5": 11,
            "24.5": 10,
            "20.8": 9,
            "17.2": 8,
            "13.9": 7,
            "10.8": 6,
            "8.0": 5,
            "5.5": 4,
            "3.4": 3,
            "1.6": 2,
            "0.3": 1,
            "-1": 0,
        }

        for key, value in mapping_text.items():
            if self._wind_avg > float(key):
                return value
        return None

    @property
    def beaufort_description(self) -> str:
        """Beaufort Textual Description."""

        if self._wind_avg is None:
            return None

        mapping_text = {
            "32.7": "hurricane",
            "28.5": "violent_storm",
            "24.5": "storm",
            "20.8": "strong_gale",
            "17.2": "fresh_gale",
            "13.9": "moderate_gale",
            "10.8": "strong_breeze",
            "8.0": "fresh_breeze",
            "5.5": "moderate_breeze",
            "3.4": "gentle_breeze",
            "1.6": "light_breeze",
            "0.3": "light_air",
            "-1": "calm",
        }

        for key, value in mapping_text.items():
            if self._wind_avg > float(key):
                return value
        return None

    @property
    def brightness(self) -> int:
        """Brightness."""
        return self._brightness

    @property
    def cloud_base(self) -> float:
        """Cloud Base (km)."""
        if self._elevation is None or self._air_temperature is None or self._dew_point is None:
            return None

        return (self._air_temperature - self._dew_point) * 126 + self._elevation

    @property
    def delta_t(self) -> float:
        """Delta_T temperature."""
        return self._delta_t

    @property
    def dew_point(self) -> float:
        """Dew Point."""
        return self._dew_point

    @property
    def feels_like(self) -> float:
        """Apparent temperature."""
        return self._feels_like

    @property
    def freezing_altitude(self) -> float:
        """Freezing Altitude."""
        if self._elevation is None or self._air_temperature is None:
            return None

        _freezing_line = (192 * self._air_temperature) + self._elevation
        return 0 if _freezing_line < 0 else _freezing_line

    @property
    def heat_index(self) -> float:
        """Heat Index."""
        return self._heat_index

    @property
    def is_freezing(self) -> bool:
        """Return if frost outside."""
        if self._air_temperature is None:
            return None
        return self._air_temperature < 0

    @property
    def is_lightning(self) -> bool:
        """Return if lightning strikes."""
        if self._lightning_strike_count is None:
            return None
        return self._lightning_strike_count > 0

    @property
    def is_raining(self) -> bool:
        """Return if raining."""
        if self._precip is None:
            return None
        return self._precip > 0

    @property
    def lightning_strike_count(self) -> int:
        """Ligntning Strike count."""
        return self._lightning_strike_count

    @property
    def lightning_strike_count_last_1hr(self) -> int:
        """Lightning strike count last hour."""
        return self._lightning_strike_count_last_1hr

    @property
    def lightning_strike_count_last_3hr(self) -> int:
        """Lightning strike count last 3 hours."""
        return self._lightning_strike_count_last_3hr

    @property
    def lightning_strike_last_distance(self) -> int:
        """Distance last lif´ghtning strike."""
        return self._lightning_strike_last_distance

    @property
    def lightning_strike_last_epoch(self) -> int:
        """Last lightning strike epoch time."""
        return self._lightning_strike_last_epoch

    @property
    def power_save_mode(self) -> int:
        """Power Save Mode (Tempest devices)."""
        if self._voltage is None:
            return None

        _solar_radiation = self._solar_radiation
        if _solar_radiation is None:
            _solar_radiation = 50

        _power_save_mode = None
        if self._voltage >= 2.455:
            _power_save_mode = 0
        elif self._voltage <= 2.355:
            _power_save_mode = 3
        elif _solar_radiation > 100:
            # Assume charging and Voltage is increasing
            if self._voltage >= 2.41:
                _power_save_mode = 1
            elif self._voltage > 2.375:
                _power_save_mode = 2
            else:
                _power_save_mode = 3
        else:
            # Assume discharging and voltage is decreasing
            if self._voltage > 2.415:
                _power_save_mode = 0
            elif self._voltage > 2.39:
                _power_save_mode = 1
            elif self._voltage > 2.355:
                _power_save_mode = 2
            else:
                _power_save_mode = 3

        return _power_save_mode

    @property
    def precip(self) -> float:
        """Precipitation."""
        return self._precip

    @property
    def precip_rate(self) -> float:
        """Precipitation Rate."""
        if self._precip is None:
            return None
        return self._precip * 60

    @property
    def precip_accum_last_1hr(self) -> float:
        """Precipitation last hour."""
        return self._precip_accum_last_1hr

    @property
    def precip_accum_local_day(self) -> float:
        """Prepitation current day."""
        return self._precip_accum_local_day

    @property
    def precip_accum_local_yesterday(self) -> float:
        """Precipitation yesterday."""
        return self._precip_accum_local_yesterday

    @property
    def precip_intensity(self) -> str:
        """Return a string with precipitation intensity."""
        if self._precip is None:
            return None

        mapping_text = {
            "0.01": "no_rain",
            "0.25": "very_light",
            "1": "light",
            "4": "moderate",
            "16": "heavy",
            "50": "very_heavy",
            "1000": "extreme",
        }

        for key, value in mapping_text.items():
            if (self._precip * 60) < float(key):
                return value
        return None

    @property
    def precip_minutes_local_day(self) -> int:
        """Precipitation minutes today."""
        return self._precip_minutes_local_day

    @property
    def precip_minutes_local_yesterday(self) -> int:
        """Precipitation minutes yesterday."""
        return self._precip_minutes_local_yesterday

    @property
    def precip_accum_local_day_final(self) -> float:
        """Prepitation current day (Rain Check)."""
        return self._precip_accum_local_day_final

    @property
    def precip_accum_local_yesterday_final(self) -> float:
        """Precipitation yesterday (Rain Check)."""
        return self._precip_accum_local_yesterday_final

    @property
    def precip_minutes_local_day_final(self) -> int:
        """Precipitation minutes today (Rain Check)."""
        return self._precip_minutes_local_day_final

    @property
    def precip_minutes_local_yesterday_final(self) -> int:
        """Precipitation minutes yesterday (Rain Check)."""
        return self._precip_minutes_local_yesterday_final

    @property
    def precip_type(self) -> str:
        """Return precipitation type."""
        return self._precipitation_type

    @property
    def pressure_trend(self) -> str:
        """Pressure trend text."""
        return self._pressure_trend

    @property
    def relative_humidity(self) -> int:
        """Relative humidity (%)."""
        return self._relative_humidity

    @property
    def sea_level_pressure(self) -> float:
        """Sea level pressure."""
        return self._sea_level_pressure

    @property
    def solar_radiation(self) -> float:
        """Solar Radiation."""
        return self._solar_radiation

    @property
    def station_name(self) -> str:
        """Station name."""
        return self._station_name

    @property
    def station_pressure(self) -> float:
        """Station pressure."""
        return self._station_pressure

    @property
    def timestamp(self) -> int:
        """Time of data update."""
        return self._timestamp

    @property
    def uv(self) -> float:
        """UV index."""
        return self._uv

    @property
    def uv_description(self) -> str:
        """UV value description."""
        if self._uv is None:
            return None

        mapping_text = {
            "10.5": "extreme",
            "7.5": "very-high",
            "5.5": "high",
            "2.8": "moderate",
            "0": "low",
        }

        for key, value in mapping_text.items():
            if self._uv >= float(key):
                return value
        return None


    @property
    def visibility(self) -> float:
        """Visibility (km)."""
        if self._elevation is None or self._air_temperature is None or self._relative_humidity is None or self._dew_point is None:
            return None

        _elevation_min = float(2)
        if self._elevation > 2:
            _elevation_min = self._elevation

        _max_visibility = float(3.56972 * math.sqrt(_elevation_min))
        _percent_reduction_a = float((1.13 * abs(self._air_temperature - self._dew_point) - 1.15) / 10)
        if _percent_reduction_a > 1:
            _percent_reduction = float(1)
        elif _percent_reduction_a < 0.025:
            _percent_reduction = 0.025
        else:
            _percent_reduction = _percent_reduction_a

        return float(_max_visibility * _percent_reduction)

    @property
    def voltage(self) -> float:
        """Return voltage of device."""
        return self._voltage

    @property
    def wet_bulb_globe_temperature(self) -> float:
        """Wet bulb globe temperature."""
        return self._wet_bulb_globe_temperature

    @property
    def wet_bulb_temperature(self) -> float:
        """Wet bulb temperature."""
        return self._wet_bulb_temperature

    @property
    def wind_avg(self) -> float:
        """Wind speed."""
        return self._wind_avg

    @property
    def wind_cardinal(self) -> str:
        """Wind Cardinal."""
        if self._wind_direction is None:
            return None

        direction_array = ["n", "nne", "ne", "ene", "e", "ese", "se", "sse", "s", "ssw", "sw", "wsw", "w", "wnw", "nw", "nnw", "n"]
        return direction_array[int((self._wind_direction + 11.25) / 22.5)]

    @property
    def wind_chill(self) -> float:
        """Wind chill factor."""
        return self._wind_chill

    @property
    def wind_direction(self) -> int:
        """Wind direction in degrees."""
        return self._wind_direction

    @property
    def wind_gust(self) -> float:
        """Wind gust speed."""
        return self._wind_gust

    @property
    def wind_lull(self) -> float:
        """Wind lull speed."""
        return self._wind_lull
