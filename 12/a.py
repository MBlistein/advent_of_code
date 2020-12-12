#!/usr/bin/env python3

"""Simply execute instructions as given.
Angles can only be [0, 90, 180, 270]; model them as integers 0 - 3."""


import fileinput


def sol(lines):
    instructions = []
    for l in lines:
        instructions.append(tuple([l[0], int(l[1:])]))

    x = y = 0
    angle = 0
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
            angle = (angle - (val // 90)) % 4
        elif cmd == 'L':
            angle = (angle + (val // 90)) % 4
        else:
            # F: move along direction specified by angle
            x += [1, 0, -1, 0][angle] * val
            y += [0, 1, 0, -1][angle] * val

    print(abs(x) + abs(y))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
