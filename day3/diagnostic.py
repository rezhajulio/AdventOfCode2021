import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map


class Submarine:
    def __init__(self, data):
        self.data = data
        self.gamma_rate, self.epsilon_rate = self.calculate_power()
        self.o2_rating = self.calculate_life_support(lambda x, y: x >= y)
        self.co2_rating = self.calculate_life_support(lambda x, y: x < y)

    @staticmethod
    def count_bits(data, position):
        """
        Count how many '1' bit in a string
        """
        return len(list(filter(lambda row: row[position] == '1', data)))

    def calculate_power(self):
        gamma_bits = ''
        epsilon_bits = ''

        for index in range(len(self.data[0])):
            # Most common bit will be larger than half of len(data)
            if self.count_bits(self.data, index) > len(self.data) / 2:
                gamma_bits += '1'
                epsilon_bits += '0'
            else:
                gamma_bits += '0'
                epsilon_bits += '1'

        return int(gamma_bits, 2), int(epsilon_bits, 2)

    def calculate_life_support(self, func):
        index = 0
        support_data = copy.copy(self.data)
        while len(support_data) > 1:
            # filtering the list based on bit criteria
            if func(self.count_bits(support_data, index), len(support_data) / 2):
                support_data = list(filter(lambda x: x[index] == '1', support_data))
            else:
                support_data = list(filter(lambda x: x[index] == '0', support_data))
            index += 1

        return int(support_data[0], 2)

    @property
    def power_consumption(self):
        return self.gamma_rate * self.epsilon_rate

    @property
    def life_support(self):
        return self.o2_rating * self.co2_rating


if __name__ == "__main__":
    data = read_map("input.txt", str)
    submarine = Submarine(data)
    print(f"Answer for Q1 is : {submarine.power_consumption}")
    print(f"Answer for Q2 is : {submarine.life_support}")
