import math
from abc import ABC, abstractmethod

from task3.app.calculator import HeightShape, Shape
from task3.app.calculator_2d import Rectangle, Square, Circle


class Shape3D(Shape, ABC):

    @abstractmethod
    def get_volume(self) -> None:
        pass


class Sphere(Shape3D):
    def __init__(self, radius: float) -> None:
        """

        :param radius: Radius of the sphere
        """
        super().__init__()
        self.radius = radius

    def get_area(self) -> float:
        """

        :return: Area of the sphere surface
        """
        return 4 * math.pi * self.radius ** 2

    def get_volume(self) -> float:
        """

        :return: Volume of the sphere
        """
        return 4 / 3 * math.pi * self.radius ** 3


class Cuboid(Shape3D):
    def __init__(self, a: float, b: float, h: float) -> None:
        """

        :param a: Side a of rectangular parallelepiped
        :param b: Side b rectangular parallelepiped
        :param h: Side h rectangular parallelepiped
        """
        super().__init__()
        self.a = a
        self.b = b
        self.h = h
        self.sides = [Rectangle(a, b), Rectangle(b, h), Rectangle(a, h)]

    def get_area(self) -> float:
        """

        :return: Area of Rectangular Parallelepiped
        """
        sides_areas = [side.get_area() for side in self.sides]
        return sum(sides_areas) * 2

    def get_volume(self) -> float:
        """

        :return: Volume of Rectangular Parallelepiped
        """
        return self.a * self.b * self.h


class Cube(Cuboid):
    def __init__(self, x: float) -> None:
        """

        :param x: Side x of the cube
        """
        super().__init__(x, x, x)

    @property
    def x(self):
        return self.a


class Cylinder(Shape3D, HeightShape):
    def __init__(self, radius: float, height: float) -> None:
        """

        :param radius: Radius of the cylinder
        :param height: Height of the cylinder
        """
        super().__init__()
        self.circle = Circle(radius)
        self.height = height

    def get_area(self) -> float:
        """

        :return: Area of the cylinder
        """
        return self.circle.get_perimeter() * self.height + 2 * self.circle.get_area()

    def get_volume(self) -> float:
        """

        :return: Volume of the cylinder
        """
        return self.circle.get_area() * self.height

    def get_height(self) -> float:
        """

        :return: Height of the cylinder
        """
        return self.height

    @property
    def radius(self):
        return self.circle.radius


class RightCircularCone(Cylinder):
    def __init__(self, radius: float, height: float) -> None:
        """

        :param radius: Radius of right circular cone
        :param height: Height of right circular cone
        """
        super().__init__(radius, height)

    def get_area(self) -> float:
        """

        :return: Area of right circular cone
        """
        side_area = math.pi * self.circle.radius * self.get_cone_generator()
        return self.circle.get_area() + side_area

    def get_volume(self) -> float:
        """

        :return: Volume of right circular cone
        """
        return (1 / 3) * self.circle.get_area() * self.height

    def get_cone_generator(self) -> float:
        """

        :return: Generator line of right circular cone
        """
        return math.sqrt(self.circle.radius ** 2 + self.height ** 2)


class SquarePyramid(Shape3D, HeightShape):
    def __init__(self, x: float, height: float) -> None:
        """

        :param x: Side x of a base square of the pyramid
        :param height: Height of the pyramid
        """
        super().__init__()
        self.square = Square(x)
        self.height = height

    @property
    def x(self):
        return self.square.x

    def get_area(self) -> float:
        """

        :return: Area of the pyramid
        """
        triangle_height = math.sqrt(self.height ** 2 + (1 / 4) * self.square.x ** 2)
        side_area = 2 * self.square.x * triangle_height
        return self.square.get_area() + side_area

    def get_volume(self) -> float:
        """

        :return: Volume of the pyramid
        """
        return (1 / 3) * self.square.get_area() * self.height

    def get_height(self) -> float:
        """

        :return: Height of the pyramid
        """
        return self.height
