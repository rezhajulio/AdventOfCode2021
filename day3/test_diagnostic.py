import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from diagnostic import Submarine


class TestDiagnostic(unittest.TestCase):
    def test_get_power_consumption(self):
        data = read_map("test_input.txt", str.strip)
        submarine = Submarine(data)
        result = submarine.power_consumption
        self.assertEqual(result, 198)

    def test_get_life_support(self):
        data = read_map("test_input.txt", str.strip)
        submarine = Submarine(data)
        result = submarine.life_support
        self.assertEqual(result, 230)


if __name__ == '__main__':
    unittest.main()
