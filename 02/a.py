#!/usr/bin/env python3


import fileinput


def sol(lines):
    cnt = 0
    for line in lines:
        reps, letter, pw = line.split(' ')
        letter = letter.strip(':')
        minreps, maxreps = list(map(int, reps.split('-')))
        if minreps <= pw.count(letter) <= maxreps:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
