import math
from abc import ABC, abstractmethod

from task3.app.calculator import HeightShape, Shape


class Shape2D(Shape, ABC):

    @abstractmethod
    def get_perimeter(self) -> None:
        pass


class Circle(Shape2D):

    def __init__(self, radius: float) -> None:
        """

        :param radius: Radius of the circle
        """
        super().__init__()
        self.radius = radius

    def get_area(self) -> float:
        """

        :return: Area of the circle
        """
        return math.pi * (self.radius ** 2)

    def get_perimeter(self) -> float:
        """

        :return: Perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape2D):
    def __init__(self, x: float, y: float) -> None:
        """

        :param x: Side x length of the rectangle
        :param y: Side y length of the rectangle
        """
        super().__init__()
        self.x = x
        self.y = y

    def get_area(self) -> float:
        """

        :return: Area of the rectangle
        """
        return self.x * self.y

    def get_perimeter(self) -> float:
        """

        :return: Perimeter of the rectangle
        """
        return 2 * (self.x + self.y)


class Square(Rectangle):
    def __init__(self, x) -> None:
        """

        :param x: Side x of the square
        """
        super().__init__(x, x)


class Trapezoid(Shape2D, HeightShape):
    def __init__(self, base: float, left_base_angle: float, right_base_angle: float, height: float) -> None:
        """

        :param base: Length of longer base side of the trapeze
        :param left_base_angle: Right base angle
        :param right_base_angle: Left base angle
        :param height: Height of the trapeze
        """
        super().__init__()
        self.base = base
        self.left_base_angle = left_base_angle
        self.right_base_angle = right_base_angle
        self.height = height
        self.right_side = self.get_right_leg()
        self.left_side = self.get_left_leg()
        self.upper_side = self.get_upper_base_side()

    def get_right_leg(self) -> float:
        """

        :return: Right lateral side of the trapezoid
        """
        return self.height / math.sin(math.radians(self.right_base_angle))

    def get_left_leg(self) -> float:
        """

        :return: Left lateral side of the trapezoid
        """
        return self.height / math.sin(math.radians(self.left_base_angle))

    def get_upper_base_side(self) -> float:
        """

        :return: Shorter base of the trapezoid
        """
        return self.base - self.height * (1 / math.tan(math.radians(self.left_base_angle)) + 1 / math.tan(
            math.radians(self.right_base_angle)))

    def get_height(self) -> float:
        """

        :return: Height of the trapezoid
        """
        return self.height

    def get_area(self) -> float:
        """

        :return: Area of the trapezoid
        """
        return (self.base + self.upper_side) / 2 * self.height

    def get_perimeter(self) -> float:
        """

        :return: Perimeter of the trapezoid
        """
        return self.base + self.right_side + self.left_side + self.upper_side


class Diamond(Shape2D, HeightShape):
    def __init__(self, d1: float, d2: float) -> None:
        """

        :param d1: Diagonal d1 of the diamond
        :param d2: Diagonal d2 of the diamond
        """
        super().__init__()
        self.d1 = d1
        self.d2 = d2

    def get_area(self) -> float:
        """

        :return: Area of the diamond
        """
        return 0.5 * self.d1 * self.d2

    def get_perimeter(self) -> float:
        """

        :return: Perimeter of the diamond
        """
        return 4 * math.sqrt((self.d1 / 2) ** 2 + (self.d2 / 2) ** 2)

    def get_height(self) -> float:
        """

        :return: Height of the diamond
        """
        return 2 * (self.d1 * self.d2) / self.get_perimeter()


class Triangle(Shape2D, HeightShape):
    def __init__(self, x: float, y: float, z: float) -> None:
        """

        :param x: Side x of the triangle
        :param y: Side y of the triangle
        :param z: Side z of the triangle
        """
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def get_area(self) -> float:
        """

        :return: Area of the triangle
        """
        half_perimeter = self.get_perimeter() / 2
        return math.sqrt(
            half_perimeter * (half_perimeter - self.x) * (half_perimeter - self.y) * (half_perimeter - self.z))

    def get_perimeter(self) -> float:
        """

        :return: Perimeter of the triangle
        """
        return self.x + self.y + self.z

    def get_height(self) -> tuple[float, float, float]:
        """

        :return: Height of the triangle
        """
        two_areas = 2 * self.get_area()
        return two_areas / self.x, two_areas / self.y, two_areas / self.z
