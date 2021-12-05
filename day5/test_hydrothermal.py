import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from hydrothermal import Vents


class TestHydrothermal(unittest.TestCase):
    def test_overlap(self):
        data = read_map("test_input.txt", str.strip)
        vents = Vents(data)
        result = vents.overlap
        self.assertEqual(result, 5)

    def test_diagonal_overlap(self):
        data = read_map("test_input.txt", str.strip)
        vents = Vents(data, diagonal=True)
        result = vents.overlap
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
