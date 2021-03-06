#!/usr/bin/env python3

"""Part B
Any fractional angle value is possible, but rotations are still limited to 90°
increments. Approach: don't model the angle itself at all, instead use rotation
rules to modify x and y."""


import fileinput


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
        elif cmd == 'R':
            for _ in range(0, val % 360, 90):
                y, x = -x, y  # rotate 90° clockwise
        elif cmd == 'L':
            for _ in range(0, val % 360, 90):
                y, x = x, -y  # rotate 90° counterclockwise
        else:
            sx += val * x
            sy += val * y

    print(abs(sx) + abs(sy))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
