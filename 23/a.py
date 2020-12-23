#!/usr/bin/env python3

"""Template for AOC python scripts"""


import fileinput


N = int(input())


def sol(lines):
    lst = list(map(int, list(lines[0])))
    idx = 0
    step = 1
    print(lst)
    n = len(lst)
    for _ in range(N):
        print()
        lst = rotate(lst, idx)
        idx = (idx + 1) % n
        print(f"After step {step}: {lst}")
        step += 1


def rotate(L, start_idx):
    """make start element first element in list --> process --> rotate back"""
    n = len(L)
    new = L[start_idx:] + L[:start_idx]
    nxt_smaller = new[0] - 1
    if nxt_smaller == 0:
        nxt_smaller = 9
    print('new:', new)

    removed = new[1: 4]
    new = [new[0]] + new[4:]
    print('cut:', new)

    for _ in range(3):
        if nxt_smaller in removed:
            nxt_smaller -= 1
            if nxt_smaller == 0:
                nxt_smaller = 9

    for kdx in range(1, len(new)):
        if new[kdx] == nxt_smaller:
            new = new[:kdx + 1] + removed + new[kdx + 1: ]
            print(f'insert at idx {kdx}')
            break
        else:
            print(f'{new}[{kdx}] = {new[kdx]} != {nxt_smaller}')
    print('ins:', new)

    return new[-start_idx:] + new[: -start_idx]  # rotate back


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
