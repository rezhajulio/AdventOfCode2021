import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from bingo import Bingo


class TestBingo(unittest.TestCase):
    def test_first_winner_board(self):
        data = list(filter(None, read_map("test_input.txt", str.strip)))
        bingo = Bingo(data)
        bingo.play()
        result = bingo.get_winning_board(0)
        self.assertEqual(result, 4512)

    def test_last_winner_board(self):
        data = list(filter(None, read_map("test_input.txt", str.strip)))
        bingo = Bingo(data)
        bingo.play()
        result = bingo.get_winning_board(-1)
        self.assertEqual(result, 1924)

    def test_check_bingo(self):
        self.assertTrue(Bingo.check_bingo([0, 13, 7, 10, 16], [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13]))


if __name__ == '__main__':
    unittest.main()
