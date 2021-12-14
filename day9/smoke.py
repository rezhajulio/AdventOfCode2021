import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from math import prod


class Basin:
    def __init__(self, data):
        self.data = data
        self.sum_low_points = 0
        self.product_of_big_three_basins = 0
        self.calculate_basins()

    @staticmethod
    def get_low_points(data):
        caves = [[*map(int, i)] for i in data]
        length = len(caves[0])
        height = len(caves)
        low_points = []
        for x in range(height):
            for y in range(length):
                point = caves[x][y]
                neighbor_positions = [z for z in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]] if
                                      height > z[0] > -1 and length > z[1] > -1]
                neighbors = [caves[p[0]][p[1]] for p in neighbor_positions]
                higher_neighbor_count = sum([1 for i in neighbors if i <= point])

                # neighbors is all higher than current point
                if higher_neighbor_count == 0:
                    low_points += [[x, y]]
        return caves, low_points, length, height

    def calculate_basins(self):
        caves, low_points, length, height = self.get_low_points(self.data)
        self.sum_low_points = sum([caves[point[0]][point[1]] for point in low_points]) + len(low_points)

        basins = []

        # checking neighbors from each low point
        for x, y in low_points:
            next_checks = [[x, y]]
            basin = []

            # check all neighbors until exhausted
            while len(next_checks) > 0:
                current_point = next_checks[0]
                next_checks = next_checks[1:]

                # get all neighbor position from current point
                neighbor_positions = [point for point in
                                      [[current_point[0] - 1, current_point[1]],
                                       [current_point[0] + 1, current_point[1]],
                                       [current_point[0], current_point[1] - 1],
                                       [current_point[0], current_point[1] + 1]]
                                      if height > point[0] > -1 and length > point[1] > -1]

                # filter neighbor if its not the heighest point
                neighbors = list(filter(lambda point: caves[point[0]][point[1]] != 9, neighbor_positions))

                # check these neighbors next
                next_checks += neighbors

                # mark current point as highest to prevent infinite loop when checking neighbors
                caves[current_point[0]][current_point[1]] = 9

                basin.append(tuple(current_point))

            # append basin size
            basins.append(len(set(basin)))

        self.product_of_big_three_basins = prod(sorted(basins, reverse=True)[:3])


if __name__ == "__main__":
    data = read_map("input.txt", str.strip)
    basin = Basin(data)
    print(f"Answer for Q1 is : {basin.sum_low_points}")
    print(f"Answer for Q2 is : {basin.product_of_big_three_basins}")
