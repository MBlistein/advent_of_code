#!/usr/bin/env python3

import fileinput


def sol(lines):
    n = len(lines)
    s = set()  # Identity of union operator
    res = 0
    for idx, line in enumerate(lines):
        if line != '':
            s |= set(line)
        if line == '' or idx == n-1:
            res += len(s)
            s = set()

    print(res)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
