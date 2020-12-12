#!/usr/bin/env python3

"""Part B
Alternative approach: calculate rotation with a standard rotation matrix valid
for any angle. Since for this problem we know that we'll always end up on
integer coordinates, we can round after every rotation."""


import fileinput
from math import cos, pi, sin


def sol(lines):
    instructions = []
    for l in lines:
        instructions.append(tuple([l[0], int(l[1:])]))

    x = 10
    y = 1
    sx = sy = 0
    for cmd, val in instructions:
        if cmd == 'E':
            x += val
        elif cmd == 'N':
            y += val
        elif cmd == 'W':
            x -= val
        elif cmd == 'S':
            y -= val
        elif cmd in 'LR':
            angle = [1, -1][cmd == 'R'] * pi * (val / 180)
            x_ = cos(angle) * x - sin(angle) * y
            y_ = sin(angle) * x + cos(angle) * y
            # we know we'll land on integer coords --> eliminate float error
            x, y = round(x_), round(y_)
        else:
            sx += val * x
            sy += val * y

    print(abs(sx) + abs(sy))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
