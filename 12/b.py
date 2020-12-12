#!/usr/bin/env python3

"""Part B
Any fractional angle value is possible, but rotations are still limited to 90°
increments --> don't model the angle itself at all, translate rotations into
a short set of rotation rules instead."""


import fileinput


def sol(lines):
    instructions = []
    for l in lines:
        instructions.append(tuple([l[0], int(l[1:])]))

    x = 10
    y = 1
    sx = sy = 0
    for f, val in instructions:
        if f == 'E':
            x += val
        elif f == 'N':
            y += val
        elif f == 'W':
            x -= val
        elif f == 'S':
            y -= val
        elif f in ('R', 'L'):
            val %= 360
            if (f, val) in [('R', 90), ('L', 270)]:
                y, x = -x, y
            elif val == 180:
                y, x = -y, -x
            elif (f, val) in [('R', 270), ('L', 90)]:
                y, x = x, -y
        else:
            sx += val * x
            sy += val * y

    print(abs(sx) + abs(sy))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
