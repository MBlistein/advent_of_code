#!/usr/bin/env python3

"""Simple Brute Force"""


import fileinput
from collections import defaultdict


def sol(lines, num_turns):
    nums = list(map(int, lines[0].split(',')))
    d = defaultdict(list)
    for idx, num in enumerate(nums):
        d[num].append(idx + 1)

    last = nums[-1]
    for i in range(len(nums) + 1, num_turns + 1):
        if len(d[last]) == 1:
            cur = 0
        else:
            cur = d[last][-1] - d[last][-2]
        d[cur].append(i)
        if len(d[cur]) > 2:
            d[cur].pop(0)
        last = cur
    print(i, last)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    num_turns = input("Enter an integer (number of turns the elves play): ")
    sol(lines, int(num_turns))
