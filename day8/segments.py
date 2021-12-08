import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_map


class Segment:
    UNIQUE_SEGMENTS = {2: 1, 4: 4, 3: 7, 7: 8}
    INTERSECTION_SEGMENTS = {5: {3: 2, 5: 3, 4: 5}, 6: {5: 0, 4: 6, 6: 9}}

    def __init__(self, data):
        self.data = data
        self.total_unique_segments = 0
        self.total_output = 0
        self.decode_segments()

    def decode_segments(self):
        """
        Counting unique segments of 1, 4, 7, 8
        1 => 2 segments
        4 => 4 segments
        7 => 3 segments
        8 => 7 segments

        for the rest of the segments
        we will use the length of the segments and
        the total of intersection with known unique segments

        From example:

        acedgfb: 8
        cdfbe: 5
        gcdfa: 2
        fbcad: 3
        dab: 7
        cefabd: 9
        cdfgeb: 6
        eafb: 4
        cagedb: 0
        ab: 1

        We will try to make a unique mapping for 0
        len("cagedb") = 6
        len(set("cagedb").intersection("ab")) = 2
        len(set("cagedb").intersection("eafb")) = 3

        So we make a dictionary where
        dict[6][2+3] = 0

        continue with the rest
        dict[5][3] = 2
        dict[5][5] = 3
        dict[5][4] = 5
        dict[6][4] = 6
        dict[6][6] = 9
        """

        for line in self.data:
            signals, outputs = line.split(" | ")

            # sorting each signal and output for mapping usage
            signals = ["".join(sorted(signal)) for signal in signals.split()]
            outputs = ["".join(sorted(output)) for output in outputs.split()]

            for pattern in outputs:
                if len(pattern) in self.UNIQUE_SEGMENTS.keys():
                    self.total_unique_segments += 1

            # mapping signals and output
            mapped_signals = [str for _ in range(10)]
            non_unique_signals = []

            for signal in signals:
                if len(signal) in self.UNIQUE_SEGMENTS:
                    # map signal from unique known pattern
                    mapped_signals[self.UNIQUE_SEGMENTS[len(signal)]] = signal
                else:
                    non_unique_signals.append(signal)

            # deduced unknown signal
            for signal in non_unique_signals:
                total_intersection = len(set(signal).intersection(mapped_signals[1])) + len(
                            set(signal).intersection(mapped_signals[4]))
                index = (self.INTERSECTION_SEGMENTS[len(signal)][total_intersection])
                mapped_signals[index] = signal

            self.total_output += int("".join(str(mapped_signals.index(output)) for output in outputs))


if __name__ == "__main__":
    data = read_map("input.txt", str.strip)
    segment = Segment(data)
    print(f"Answer for Q1 is : {segment.total_unique_segments}")
    print(f"Answer for Q2 is : {segment.total_output}")
