import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map


def count_increased(data, window_size):
    """
    Count current window data with the previous window if its smaller
    :param data: list of integer
    :param window_size: windows size of comparison
    :return: count where current window is larger than previous window

    199  A
    200  A B
    208  A B C
    210    B C D
    200  E   C D
    207  E F   D
    240  E F G
    269    F G H
    260      G H
    263        H

    If you take a look between window A and B, the intersection is 200 and 208.
    To compare this window, we don't need to make a windowing data structure, we just need to compare
    the first element of window A with the last element of window B
    """
    assert window_size > 0
    return sum([1 for i in range(window_size, len(data)) if data[i] > data[i - window_size]])


if __name__ == "__main__":
    data = read_map("input.txt", int)

    print(f"Answer for Q1 is : {count_increased(data, 1)}")
    print(f"Answer for Q1 is : {count_increased(data, 3)}")
