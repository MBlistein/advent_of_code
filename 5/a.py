#!/usr/bin/env python3

import fileinput


def sol(lines):
    ids = list(sorted([get_id(code) for code in lines]))
    print(max(ids))
    print([ids[i] + 1 for i in range(len(ids) - 1) if ids[i+1] - ids[i] == 2][0])


def get_id(code):
    """parse ticket id as binary number"""
    seat_id = 0
    for i in range(len(code)):
        seat_id <<= 1
        seat_id |= code[i] in 'BR'

    return seat_id


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
