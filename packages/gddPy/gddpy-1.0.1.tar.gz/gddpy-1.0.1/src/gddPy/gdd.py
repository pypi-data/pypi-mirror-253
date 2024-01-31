import numbers
import numpy as np


class GDD:
    """GDD class"""

    __low_temperature = None
    __high_temperature = None
    __threshold_low = None

    def __init__(self, params: dict = None):
        if params:
            if not isinstance(params, dict):
                raise TypeError("params must be a dictionary")
            if "low_temperature" in params:
                self.low_temperature = params.get("low_temperature")
            if "high_temperature" in params:
                self.high_temperature = params.get("high_temperature")
            if "threshold_low" in params:
                self.threshold_low = params.get("threshold_low")

    def set_low_temperature(self, low_temperature: float) -> None:
        if not isinstance(low_temperature, numbers.Number):
            raise TypeError("low_temperature must be a number")
        if (
            self.__high_temperature is not None
            and low_temperature > self.__high_temperature
        ):
            raise ValueError("low_temperature must be less than high_temperature")
        self.__low_temperature = low_temperature

    def set_high_temperature(self, high_temperature: float) -> None:
        if not isinstance(high_temperature, numbers.Number):
            raise TypeError("high_temperature must be a number")
        if (
            self.__low_temperature is not None
            and high_temperature < self.__low_temperature
        ):
            raise ValueError("high_temperature must be greater than low_temperature")
        self.__high_temperature = high_temperature

    def set_threshold_low(self, threshold_low: float) -> None:
        if not isinstance(threshold_low, numbers.Number):
            raise TypeError("threshold_low must be a number")
        self.__threshold_low = threshold_low

    def get_low_temperature(self) -> numbers.Number:
        return self.__low_temperature

    def get_high_temperature(self) -> numbers.Number:
        return self.__high_temperature

    def get_threshold_low(self) -> numbers.Number:
        return self.__threshold_low

    low_temperature = property(get_low_temperature, set_low_temperature)
    high_temperature = property(get_high_temperature, set_high_temperature)
    threshold_low = property(get_threshold_low, set_threshold_low)

    def __dailyAverage(low: float, high: float, base: float) -> numbers.Number:
        return max(0, ((high + low) / 2) - base)

    def calcDailyAverage(self):
        if self.low_temperature is None or self.high_temperature is None:
            raise ValueError("low_temperature and high_temperature must be set")

        if self.__threshold_low is None:
            raise ValueError("threshold_low must be set")

        gdd = GDD.__dailyAverage(
            self.low_temperature, self.high_temperature, self.threshold_low
        )
        return gdd

    def calcBaskervilleEmin(self) -> numbers.Number:
        if self.low_temperature is None or self.high_temperature is None:
            raise ValueError("low_temperature and high_temperature must be set")

        if self.threshold_low is None:
            raise ValueError("threshold_low must be set")

        if self.high_temperature < self.__threshold_low:
            return 0
        elif self.low_temperature >= self.__threshold_low:
            return GDD.__dailyAverage(
                self.low_temperature, self.high_temperature, self.threshold_low
            )
        else:
            avg = (self.low_temperature + self.high_temperature) / 2
            w = (self.high_temperature - self.low_temperature) / 2
            arcsin = np.arcsin((self.__threshold_low - avg) / w)

            gdd = (
                w * np.cos(arcsin) - (self.__threshold_low - avg) * (np.pi / 2 - arcsin)
            ) / np.pi
            return gdd
