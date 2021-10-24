from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def get_area(self) -> None:
        pass


class HeightShape(Shape, ABC):

    @abstractmethod
    def get_height(self) -> None:
        pass


class ResultPrinter:

    @staticmethod
    def round_result(value: float, decimal_places: int = 3) -> float:
        """

        :param value: The value to be rounded
        :param decimal_places: The precision after the decimal point the value should be rounded to
        :return: Number rounded to decimal_places precision
        """
        return round(value, decimal_places)
