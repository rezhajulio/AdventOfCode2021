import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map


class Submarine:
    def __init__(self, data):
        self.horizontal = 0
        self.vertical = 0
        self.aim = 0
        self.depth = 0
        self.data = data
        self.actions = {
            "forward": self.forward,
            "up": self.up,
            "down": self.down
        }
        self.run_actions()

    def forward(self, step):
        self.horizontal += step
        self.depth += self.aim * step

    def down(self, step):
        self.vertical += step
        self.aim += step

    def up(self, step):
        self.vertical -= step
        self.aim -= step

    def run_actions(self):
        for action, step in self.data:
            self.actions[action](int(step))

    @property
    def position(self):
        return self.horizontal * self.vertical

    @property
    def actual_position(self):
        return self.horizontal * self.depth


if __name__ == "__main__":
    data = read_map("input.txt", str.split)
    submarine = Submarine(data)
    print(f"Answer for Q1 is : {submarine.position}")
    print(f"Answer for Q2 is : {submarine.actual_position}")
