import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from collections import defaultdict


class Vents:
    def __init__(self, data, diagonal=False):
        self.data = data
        self.diagonal = diagonal
        self.vents = None
        self.diagram = defaultdict(lambda: 0)
        self.parse_data()
        self.calculate_vents()

    def parse_data(self):
        vents = []
        for datum in self.data:
            start, _, end = datum.split()
            start, end = self.parse_coordinate(start), self.parse_coordinate(end)

            vents.append((start, end))

        self.vents = vents

    def calculate_vents(self):
        for start, end in self.vents:
            # calculate horizontal line
            if start[1] == end[1]:
                # sort point first to be able to use range
                start_x_point, end_x_point = sorted((start[0], end[0]))
                for index_x in range(start_x_point, end_x_point + 1):
                    self.diagram[(index_x, start[1])] += 1
            # calculate vertical line
            elif start[0] == end[0]:
                start_y_point, end_y_point = sorted((start[1], end[1]))
                for index_y in range(start_y_point, end_y_point + 1):
                    self.diagram[(start[0], index_y)] += 1
            # calculate diagonal
            else:
                # calculate if flag is enabled
                if self.diagonal:
                    dx, dy = self.calculate_gradient(*sorted((start, end)))
                    (start_x_point, start_y_point), (end_x_point, end_y_point) = sorted((start, end))

                    while True:
                        self.diagram[(start_x_point, start_y_point)] += 1
                        if start_x_point == end_x_point and start_y_point == end_y_point:
                            break

                        start_x_point += dx
                        start_y_point += dy

    @staticmethod
    def calculate_gradient(start, end):
        dx = start[0] - end[0]
        dy = start[1] - end[1]
        dx = dx // abs(dx)
        dy = dy // abs(dy)

        if dx < 0 and dy < 0:
            return abs(dx), abs(dy)
        elif dx < 0 < dy:
            return dy, dx
        return dx, dy

    @staticmethod
    def parse_coordinate(string):
        return tuple(map(int, string.split(",")))

    @property
    def overlap(self):
        # overlap points should be 2 or larger
        return sum(1 for _ in filter(lambda item: item > 1, self.diagram.values()))


if __name__ == "__main__":
    data = read_map("input.txt", str.strip)
    vents = Vents(data)
    print(f"Answer for Q1 is : {vents.overlap}")
    # need to recalculate diagram with diagonal
    vents = Vents(data, diagonal=True)
    print(f"Answer for Q2 is : {vents.overlap}")
