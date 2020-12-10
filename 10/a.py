#!/usr/bin/env python3

"""part A: sort adapters and count gaps between them"""


import fileinput
from collections import Counter


def sol(lines):
    adapters = [int(a) for a in lines]
    adapters += [0, max(adapters) + 3]  # add socket and built-in
    adapters.sort()

    gaps = Counter()
    for i in range(len(adapters) - 1):
        gaps[adapters[i+1] - adapters[i]] += 1

    print(gaps[1] * gaps[3])


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
