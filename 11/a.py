#!/usr/bin/env python3

"""Simulate seat occupancy fluctuation in a brute force way:
At every step, check every seat's neighbors and update accordingly."""

import copy
import fileinput
from typing import List


def num_occupied_neighbors(grid: List[List[str]], r: int, c: int) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    num_occ = 0
    for dr in range(-1, 2, 1):
        for dc in range(-1, 2, 1):
            if dr == dc == 0:
                continue
            if (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
                num_occ += grid[r + dr][c + dc] == '#'
    return num_occ


def num_occupied_visible(grid: List[List[str]], r: int, c: int) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    num_occ = 0
    for dr in range(-1, 2, 1):
        for dc in range(-1, 2, 1):
            if dr == dc == 0:
                continue
            row, col = r, c
            while True:
                row += dr
                col += dc
                if not (0 <= row < num_rows and 0 <= col < num_cols):
                    break  # outside grid
                if grid[row][col] != '.':
                    num_occ += grid[row][col] == '#'
                    break
    return num_occ


def sol(lines: List[str], partA: bool) -> int:
    grid = [list(line) for line in lines]
    num_rows, num_cols = len(grid), len(grid[0])
    change = True
    while change:
        change = False
        new = copy.deepcopy(grid)
        for r in range(num_rows):
            for c in range(num_cols):
                if new[r][c] == '.':
                    continue
                num_occ = num_occupied_neighbors(grid, r, c) if partA else num_occupied_visible(grid, r, c)
                if new[r][c] == 'L' and num_occ == 0:
                    new[r][c] = '#'
                    change = True
                elif new[r][c] == '#' and num_occ >= (4 if partA else 5):
                    new[r][c] = 'L'
                    change = True
        grid = new

    occ_seats = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == '#':
                occ_seats += 1
    return occ_seats


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    print('part A:', sol(lines, True))
    print('part B:', sol(lines, False))
