#!/usr/bin/env python3

import fileinput
import string


def sol(lines):
    res = 0
    s = set(string.ascii_lowercase)  # Identity of intersect op (for this case)
    n = len(lines)
    for idx, line in enumerate(lines):
        if line != '':
            s &= set(line)
        if line == '' or idx == n-1:
            res += len(s)
            s = set(string.ascii_lowercase)

    print(res)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
