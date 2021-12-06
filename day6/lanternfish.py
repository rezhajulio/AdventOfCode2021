import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map
from collections import defaultdict, Counter


class Lanternfish:
    def __init__(self, data):
        self.data = data

    def growth(self, days):
        current_population = Counter(map(int, self.data[0].split(",")))

        for day in range(days):
            tomorrow_population = defaultdict(lambda: 0)

            for timer, count in current_population.items():
                if timer == 0:
                    # reset those with timer 0 to 6
                    tomorrow_population[6] += count
                    # add new fish with timer 8
                    tomorrow_population[8] += count
                else:
                    # reduce timer by 1
                    tomorrow_population[timer - 1] += count

            current_population = tomorrow_population
        return sum(current_population.values())


if __name__ == "__main__":
    data = read_map("input.txt", str.strip)
    lanternfish = Lanternfish(data)
    print(f"Answer for Q1 is : {lanternfish.growth(80)}")
    print(f"Answer for Q2 is : {lanternfish.growth(256)}")
