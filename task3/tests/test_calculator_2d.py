import unittest

from task3.app.calculator import ResultPrinter
from task3.app.calculator_2d import Circle, Rectangle, Square, Diamond, Triangle, Trapezoid


class TestCircle(unittest.TestCase):
    radius = 2

    def setUp(self):
        self.test_circle = Circle(self.radius)

    def test_area_calculation(self):
        area = self.test_circle.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 12.566)

    def test_perimeter_calculation(self):
        perimeter = self.test_circle.get_perimeter()
        self.assertEqual(ResultPrinter.round_result(perimeter), 12.566)


class TestRectangle(unittest.TestCase):
    x, y = 2, 5

    def setUp(self):
        self.test_rectangle = Rectangle(self.x, self.y)

    def test_area_calculation(self):
        area = self.test_rectangle.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 10)

    def test_perimeter_calculation(self):
        perimeter = self.test_rectangle.get_perimeter()
        self.assertEqual(ResultPrinter.round_result(perimeter), 14)


class TestSquare(unittest.TestCase):
    x = 3

    def setUp(self):
        self.test_square = Square(self.x)

    def test_area_calculation(self):
        area = self.test_square.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 9)

    def test_perimeter_calculation(self):
        perimeter = self.test_square.get_perimeter()
        self.assertEqual(ResultPrinter.round_result(perimeter), 12)


class TestDiamond(unittest.TestCase):
    d1, d2 = 3, 4

    def setUp(self):
        self.test_diamond = Diamond(self.d1, self.d2)

    def test_area_calculation(self):
        area = self.test_diamond.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 6)

    def test_perimeter_calculation(self):
        perimeter = self.test_diamond.get_perimeter()
        self.assertEqual(ResultPrinter.round_result(perimeter), 10)

    def test_height_calculation(self):
        pass


class TestTriangle(unittest.TestCase):
    x, y, z = 2, 3, 4

    def setUp(self):
        self.test_triangle = Triangle(self.x, self.y, self.z)

    def test_area_calculation(self):
        area = self.test_triangle.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 2.905)

    def test_perimeter_calculation(self):
        perimeter = self.test_triangle.get_perimeter()
        self.assertEqual(ResultPrinter.round_result(perimeter), 9)

    def test_height_calculation(self):
        heights = self.test_triangle.get_height()
        heights = [ResultPrinter.round_result(height) for height in heights]
        self.assertEqual(heights, [2.905, 1.936, 1.452])


class TestTrapeze(unittest.TestCase):
    base = 2
    left_base_angle = 90
    right_base_angle = 45
    height = 1

    def setUp(self):
        self.test_trapeze = Trapezoid(self.base, self.left_base_angle, self.right_base_angle, self.height)

    def test_right_side_calculation(self):
        right_side = self.test_trapeze.get_right_leg()
        self.assertEqual(ResultPrinter.round_result(right_side), 1.414)

    def test_left_side_calculation(self):
        left_side = self.test_trapeze.get_left_leg()
        self.assertEqual(ResultPrinter.round_result(left_side), 1)

    def test_upper_side_calculation(self):
        upper_side = self.test_trapeze.get_upper_base_side()
        self.assertEqual(ResultPrinter.round_result(upper_side), 1)

    def test_height_calculation(self):
        height = self.test_trapeze.get_height()
        self.assertEqual(ResultPrinter.round_result(height), 1)

    def test_area_calculation(self):
        area = self.test_trapeze.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 1.5)

    def test_perimeter_calculation(self):
        perimeter = self.test_trapeze.get_perimeter()
        self.assertEqual(ResultPrinter.round_result(perimeter), 5.414)
