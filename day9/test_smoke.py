import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from smoke import Basin


class TestBasin(unittest.TestCase):
    def test_sum_low_point(self):
        data = read_map("test_input.txt", str.strip)
        basin = Basin(data)
        result = basin.sum_low_points
        self.assertEqual(result, 15)

    def test_product_of_biggest_three_basins(self):
        data = read_map("test_input.txt", str.strip)
        basin = Basin(data)
        result = basin.product_of_big_three_basins
        self.assertEqual(result, 1134)


if __name__ == '__main__':
    unittest.main()
