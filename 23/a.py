#!/usr/bin/env python3

"""Brute force: rotate the list left, process, rotate back."""


import fileinput


def sol(lines):
    lst = list(map(int, list(lines[0])))
    idx = 0
    n = len(lst)
    for _ in range(int(input("Input number of moves: "))):
        lst = rotate(lst, idx)
        idx = (idx + 1) % n

    jdx = lst.index(1)
    print(''.join(map(str, lst[jdx+1:] + lst[:jdx])))


def rotate(L, start_idx):
    """rotate L left to make start element first element in list.
    Then process and rotate back"""
    NL = L[start_idx:] + L[:start_idx]
    nxt_smaller = (NL[0] - 1) or 9

    removed = NL[1: 4]
    NL = [NL[0]] + NL[4:]

    for _ in range(3):
        if nxt_smaller in removed:
            nxt_smaller = (nxt_smaller - 1) or 9

    for jdx in range(1, len(NL)):
        if NL[jdx] == nxt_smaller:
            NL = NL[:jdx + 1] + removed + NL[jdx + 1: ]
            break

    return NL[-start_idx:] + NL[: -start_idx]  # rotate back


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
