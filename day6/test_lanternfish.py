import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from lanternfish import Lanternfish


class TestHydrothermal(unittest.TestCase):
    def test_growth_80_days(self):
        data = read_map("test_input.txt", str.strip)
        lanternfish = Lanternfish(data)
        result = lanternfish.growth(80)
        self.assertEqual(result, 5934)

    def test_growth_256_days(self):
        data = read_map("test_input.txt", str.strip)
        lanternfish = Lanternfish(data)
        result = lanternfish.growth(256)
        self.assertEqual(result, 26984457539)


if __name__ == '__main__':
    unittest.main()
