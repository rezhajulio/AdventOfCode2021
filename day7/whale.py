import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map


class Whale:
    CRAB = "CRAB"

    def __init__(self, data, mode=None):
        self.data = list(map(int, data.split(",")))
        self.mode = mode

    def fuel_usage(self, distance):
        if self.mode == self.CRAB:
            # the sum of the list of increasing number
            # can be counted using arithmetic progression
            return distance * (distance + 1) // 2
        return distance

    @property
    def fuel(self):
        # define as infinity number
        cheapest_fuel = float("inf")

        # calculate for best position between crabs
        for position in range(min(self.data), max(self.data) + 1):
            fuel = sum(self.fuel_usage(abs(position - crab_position)) for crab_position in self.data)
            cheapest_fuel = min(cheapest_fuel, fuel)

        return cheapest_fuel


if __name__ == "__main__":
    data = read_map("input.txt", str.strip)
    whale = Whale(data)
    print(f"Answer for Q1 is : {whale.fuel}")
    whale = Whale(data, Whale.CRAB)
    print(f"Answer for Q2 is : {whale.fuel}")
