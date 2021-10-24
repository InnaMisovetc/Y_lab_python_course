import unittest

from task3.app.calculator import ResultPrinter
from task3.app.calculator_3d import Sphere, Cuboid, Cube, Cylinder, RightCircularCone, SquarePyramid


class TestSphere(unittest.TestCase):
    radius = 2

    def setUp(self):
        self.test_sphere = Sphere(self.radius)

    def test_area_calculation(self):
        area = self.test_sphere.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 50.265)

    def test_volume_calculation(self):
        volume = self.test_sphere.get_volume()
        self.assertEqual(ResultPrinter.round_result(volume), 33.510)


class TestRectangularParallelepiped(unittest.TestCase):
    a, b, c = 2, 3, 4

    def setUp(self):
        self.test_parallelepiped = Cuboid(self.a, self.b, self.c)

    def test_area_calculation(self):
        area = self.test_parallelepiped.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 52)

    def test_volume_calculation(self):
        volume = self.test_parallelepiped.get_volume()
        self.assertEqual(ResultPrinter.round_result(volume), 24)


class TestCube(unittest.TestCase):
    x = 3

    def setUp(self):
        self.test_cube = Cube(self.x)

    def test_area_calculation(self):
        area = self.test_cube.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 54)

    def test_volume_calculation(self):
        volume = self.test_cube.get_volume()
        self.assertEqual(ResultPrinter.round_result(volume), 27)


class TestCylinder(unittest.TestCase):
    radius = 2
    height = 3

    def setUp(self):
        self.test_cylinder = Cylinder(self.radius, self.height)

    def test_area_calculation(self):
        area = self.test_cylinder.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 62.832)

    def test_volume_calculation(self):
        volume = self.test_cylinder.get_volume()
        self.assertEqual(ResultPrinter.round_result(volume), 37.699)

    def test_height_calculation(self):
        height = self.test_cylinder.get_height()
        self.assertEqual(ResultPrinter.round_result(height), 3)


class TestRightCircularCone(unittest.TestCase):
    radius = 2
    height = 3

    def setUp(self):
        self.test_cone = RightCircularCone(self.radius, self.height)

    def test_area_calculation(self):
        area = self.test_cone.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 35.221)

    def test_volume_calculation(self):
        volume = self.test_cone.get_volume()
        self.assertEqual(ResultPrinter.round_result(volume), 12.566)

    def test_height_calculation(self):
        height = self.test_cone.get_height()
        self.assertEqual(ResultPrinter.round_result(height), 3)

    def test_generator_calculation(self):
        cone_generator = self.test_cone.get_cone_generator()
        self.assertEqual(ResultPrinter.round_result(cone_generator), 3.606)


class TestSquarePyramid(unittest.TestCase):
    height = 3
    x = 2

    def setUp(self):
        self.test_pyramid = SquarePyramid(self.x, self.height)

    def test_area_calculation(self):
        area = self.test_pyramid.get_area()
        self.assertEqual(ResultPrinter.round_result(area), 16.649)

    def test_volume_calculation(self):
        volume = self.test_pyramid.get_volume()
        self.assertEqual(ResultPrinter.round_result(volume), 4)

    def test_height_calculation(self):
        height = self.test_pyramid.get_height()
        self.assertEqual(ResultPrinter.round_result(height), 3)
