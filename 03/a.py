#!/usr/bin/env python3

import fileinput


def sol(lines):
    pos = 0
    cnt = 0
    for line in lines:
        cnt += line[pos % len(line)] == '#'
        pos += 3
    print(cnt)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)

