import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from whale import Whale


class TestWhale(unittest.TestCase):
    def test_cheapest_fuel(self):
        data = read_map("test_input.txt", str.strip)[0]
        whale = Whale(data)
        result = whale.fuel
        self.assertEqual(result, 37)

    def test_cheapest_fuel_crab_mode(self):
        data = read_map("test_input.txt", str.strip)[0]
        whale = Whale(data, Whale.CRAB)
        result = whale.fuel
        self.assertEqual(result, 168)


if __name__ == '__main__':
    unittest.main()
