import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from syntax import Score


class TestScore(unittest.TestCase):
    def test_illegal_score(self):
        data = read_map("test_input.txt", str.strip)
        score = Score(data)
        result = score.illegal_score
        self.assertEqual(result, 26397)

    def test_middle_score(self):
        data = read_map("test_input.txt", str.strip)
        score = Score(data)
        result = score.middle_score
        self.assertEqual(result, 288957)


if __name__ == '__main__':
    unittest.main()
