#!/usr/bin/env python3

import fileinput  # Execute this file like this: ./b.py input_file


def sol(lines):
    cnt = 0
    for line in lines:
        reps, letter, pw = line.split()
        letter = letter.strip(':')
        i, j = list(map(int, reps.split('-')))

        if (pw[i-1] == letter) ^ (pw[j-1] == letter):
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
