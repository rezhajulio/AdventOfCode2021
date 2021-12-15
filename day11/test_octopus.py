import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from octopus import Octopus


class TestOctopus(unittest.TestCase):
    def test_total_flashes(self):
        data = read_map("test_input.txt", str.strip)
        octopus = Octopus(data)
        octopus.steps(step=100)
        result = octopus.total_flashes
        self.assertEqual(result, 1656)

    def test_when_all_flashed(self):
        data = read_map("test_input.txt", str.strip)
        octopus = Octopus(data)
        octopus.steps()
        result = octopus.all_flashed
        self.assertEqual(result, 195)


if __name__ == '__main__':
    unittest.main()
