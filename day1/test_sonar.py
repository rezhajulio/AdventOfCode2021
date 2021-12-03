import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from sonar import count_increased


class TestSonar(unittest.TestCase):
    def test_one_day_window(self):
        data = read_map("test_input.txt", int)
        result = count_increased(data, 1)
        self.assertEqual(result, 7)

    def test_three_day_window(self):
        data = read_map("test_input.txt", int)
        result = count_increased(data, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
