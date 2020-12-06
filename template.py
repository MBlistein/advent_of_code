#!/usr/bin/env python3

import fileinput


def sol(lines):
    for l in lines:
        print(l)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
