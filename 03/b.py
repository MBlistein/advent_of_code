#!/usr/bin/env python3

import fileinput


def count_trees(grid, dr, dc):
    cnt = 0
    mod = len(grid[0])
    row = col = 0
    while row < len(grid):
        cnt += grid[row][col] == '#'
        row += dr
        col = (col + dc) % mod
    return cnt


def sol(grid):
    res = 1
    for dc, dr in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        res *= count_trees(grid, dr, dc)
    print(res)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
