import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map


class Octopus:
    def __init__(self, data):
        self.data = [[int(char) for char in line] for line in data]
        self.height = len(self.data)
        self.length = len(self.data[0])
        self.total_flashes = 0
        self.all_flashed = 0

    def steps(self, step=0, all_flashed=False):
        grid = copy.copy(self.data)

        if not all_flashed:
            for _ in range(step):
                grid, flashed = self.get_step(grid)
                self.total_flashes += flashed
        else:
            step_count = 0
            while True:
                step_count += 1
                grid, flashed = self.get_step(grid)

                # stop when all octopus flashed for the first time
                if flashed == self.height * self.length:
                    self.all_flashed = step_count
                    break

    def get_neighbors(self, x, y):
        for index_x, index_y in (
                (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1),
                (x + 1, y + 1)):
            # get neighbors within range of grid
            if 0 <= index_x < self.height and 0 <= index_y < self.length:
                yield index_x, index_y

    def get_step(self, grid):
        for x in range(self.height):
            for y in range(self.length):
                grid[x][y] += 1

        flashed = set()
        changed = True

        # keep updating the grid until all octopus done flashing
        while changed:
            changed = False
            for x in range(self.height):
                for y in range(self.length):
                    if grid[x][y] > 9 and (x, y) not in flashed:
                        flashed.add((x, y))
                        for index_x, index_y in self.get_neighbors(x, y):
                            grid[index_x][index_y] += 1
                            changed = True

        # reset energy level after flashing
        for x, y in flashed:
            grid[x][y] = 0

        return grid, len(flashed)


if __name__ == "__main__":
    data = read_map("input.txt", str.strip)
    octopus = Octopus(data)
    octopus.steps(step=100)
    print(f"Answer for Q1 is : {octopus.total_flashes}")
    octopus.steps(all_flashed=True)
    print(f"Answer for Q2 is : {octopus.all_flashed}")
