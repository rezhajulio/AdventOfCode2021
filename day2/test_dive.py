import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from dive import Submarine


class TestDive(unittest.TestCase):
    def test_get_position(self):
        data = read_map("test_input.txt", str.split)
        submarine = Submarine(data)
        result = submarine.position
        self.assertEqual(result, 150)

    def test_get_actual_position(self):
        data = read_map("test_input.txt", str.split)
        submarine = Submarine(data)
        result = submarine.actual_position
        self.assertEqual(result, 900)


if __name__ == '__main__':
    unittest.main()
