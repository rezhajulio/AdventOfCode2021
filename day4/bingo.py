import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map, chunks
from itertools import chain


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.played_numbers = None

    def get_column(self, position):
        return list(map(lambda row: row[position], self.rows))

    @property
    def score(self):
        flatten_board = list(chain(*self.rows))
        unmarked_board = [item for item in flatten_board if item not in self.played_numbers]
        return sum(unmarked_board) * self.played_numbers[-1]


class Bingo:
    def __init__(self, data):
        self.data = data
        self.inputs = None
        self.boards = []
        self.winning_boards = []
        self.parse_data()

    def parse_data(self):
        self.inputs = list(map(int, self.data[0].split(",")))

        for rows in chunks(self.data[1:], 5):
            rows = [list(map(int, row.split())) for row in rows]
            self.boards.append(Board(rows))

    @staticmethod
    def check_bingo(a_list, played_numbers):
        for number in a_list:
            if number not in played_numbers:
                return False
        return True

    def play(self):
        # place first 4 numbers into played numbers
        played_numbers = self.inputs[:4]
        for number in self.inputs[4:]:
            # stop if all board already winning
            if len(self.winning_boards) == len(self.boards):
                break

            played_numbers.append(number)

            # check each board
            for board in self.boards:
                # don't check winning board
                if board in self.winning_boards:
                    continue

                # check each row
                for row in board.rows:
                    if self.check_bingo(row, played_numbers):
                        self.add_winning_board(board, played_numbers)
                        break

                # check each column
                for index in range(5):
                    column = board.get_column(index)
                    if self.check_bingo(column, played_numbers):
                        self.add_winning_board(board, played_numbers)
                        break

    def add_winning_board(self, board, played_numbers):
        board.played_numbers = copy.copy(played_numbers)
        self.winning_boards.append(board)

    def get_winning_board(self, position):
        board = self.winning_boards[position]
        return board.score


if __name__ == "__main__":
    data = list(filter(None, read_map("input.txt", str.strip)))
    bingo = Bingo(data)
    bingo.play()
    print(f"Answer for Q1 is : {bingo.get_winning_board(0)}")
    print(f"Answer for Q2 is : {bingo.get_winning_board(-1)}")
