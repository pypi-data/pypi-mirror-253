"""This module describes dataclasses used by pymeteobridgesql."""

from __future__ import annotations

import dataclasses

@dataclasses.dataclass
class RealtimeData:
    ID: str
    temperature: float
    tempmax: float
    tempmin: float
    windchill: float
    pm1: float
    pm25: float
    pm10: float
    heatindex: float
    temp15min: float
    humidity: int
    windspeedavg: float
    windgust: float
    dewpoint: float
    rainrate: float
    raintoday: float
    rainyesterday: float
    windbearing: int
    beaufort: int
    sealevelpressure: float
    uv: float
    uvdaymax: float
    solarrad: float
    solarraddaymax: float
    pressuretrend: float
    mb_ip: str
    mb_swversion: str
    mb_buildnum: str
    mb_platform: str
    mb_station: str
    mb_stationname: str
    elevation: int

    @property
    def beaufort_description(self) -> str:
        """Beaufort Textual Description."""

        if self.windspeedavg is None:
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
            if self.windspeedavg > float(key):
                return value
        return None

    @property
    def feels_like_temperature(self) -> float:
        """Calculate feels like temperature using windchill and heatindex."""
        if self.windchill is not None and self.heatindex is not None and self.temperature is not None and self.humidity is not None and self.windspeedavg is not None:
            if self.temperature > 26.7 and self.humidity > 40:
                return self.heatindex
            if self.temperature < 10 and self.windspeedavg > 4.8:
                return self.windchill
            return self.temperature
        return None

    @property
    def pressuretrend_text(self) -> str:
        """Converts the pressure trend to text."""
        if self.pressuretrend is None:
            return None

        if self.pressuretrend > 0:
            return "rising"
        if self.pressuretrend < 0:
            return "falling"
        return "steady"

    @property
    def uv_description(self) -> str:
        """UV value description."""
        if self.uv is None:
            return None

        mapping_text = {
            "10.5": "extreme",
            "7.5": "very-high",
            "5.5": "high",
            "2.8": "moderate",
            "0": "low",
        }

        for key, value in mapping_text.items():
            if self.uv >= float(key):
                return value
        return None

    @property
    def wind_direction(self) -> str:
        """Calculates the wind direction from the wind bearing."""
        if self.windbearing is None:
            return None

        directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        index = round(self.windbearing / 22.5) % 16
        return directions[index]

@dataclasses.dataclass
class StationData:
    ID: str
    mb_ip: str
    mb_swversion: str
    mb_buildnum: str
    mb_platform: str
    mb_station: str
    mb_stationname: str
