import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map


class Score:
    CLOSER = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    OPENER = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    PAIR = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    def __init__(self, data):
        self.data = data
        self.illegal_score = 0
        self.middle_score = 0
        self.process_syntax()

    def process_syntax(self):
        list_score = []

        for line in self.data:
            stack = []
            found = False

            # checking each char in for illegal line
            for index, char in enumerate(line):
                if char in self.PAIR:
                    if stack:
                        # check if last element in stack is the pair of current char
                        if stack[-1] == self.PAIR[char]:
                            stack.pop()
                        else:
                            found = index
                            break
                else:
                    stack.append(char)

            if found:
                # illegal line found
                illegal_char = line[index]
                self.illegal_score += self.CLOSER[illegal_char]
            else:
                # valid line found, count score instead
                score = 0

                while stack:
                    char = stack.pop()
                    score *= 5
                    score += self.OPENER[char]
                list_score.append(score)

        self.middle_score = sorted(list_score)[len(list_score) // 2]


if __name__ == "__main__":
    data = read_map("input.txt", str.strip)
    score = Score(data)
    print(f"Answer for Q1 is : {score.illegal_score}")
    print(f"Answer for Q2 is : {score.middle_score}")
