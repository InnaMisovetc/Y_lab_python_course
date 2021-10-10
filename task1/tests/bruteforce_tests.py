import unittest
from task1.app.bruteforce import BruteForcePlanner, Path

path_points = [(0, 0), (1, 1), (2, 1)]
best_path = Path([(0, 0), (1, 1), (2, 1), (0, 0)])
best_path_distance = 2 ** 0.5 + 1 + 5 ** 0.5


class TestPoints(unittest.TestCase):
    def test_points(self):
        planner = BruteForcePlanner(path_points)
        self.assertEqual(planner.find_best_path().points, best_path.points)


class TestTotalDistance(unittest.TestCase):
    def test_total_distance(self):
        planner = BruteForcePlanner(path_points)
        self.assertAlmostEqual(planner.find_best_path().total_distance(), best_path_distance)


if __name__ == '__main__':
    unittest.main()
