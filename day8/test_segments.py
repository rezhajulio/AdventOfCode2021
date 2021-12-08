import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from segments import Segment


class TestSegments(unittest.TestCase):
    def test_unique_segments(self):
        data = read_map("test_input.txt", str.strip)
        segment = Segment(data)
        result = segment.total_unique_segments
        self.assertEqual(result, 26)

    def test_total_output(self):
        data = read_map("test_input.txt", str.strip)
        segment = Segment(data)
        result = segment.total_output
        self.assertEqual(result, 61229)


if __name__ == '__main__':
    unittest.main()
