#!/usr/bin/env python3

"""Ensure all tile edges occurr at most twice --> tile position is
uniquely determined by a single matching edge"""


import fileinput
import sys
from copy import deepcopy


def parse_input(filepath):
    grids = {}
    with open(filepath, 'r') as file:
        big_string = file.read()
        for chunk in big_string[:-1].split('\n\n'):
            lines = [l.strip() for l in chunk.split('\n')]
            name = lines[0].split()[1][:-1]
            grids[int(name)] = list(map(list, lines[1:]))
    return grids


def rotate_left(grid, angle):
    """1 = 90°, 2 = 180°, 3 = 270°"""
    grid = deepcopy(grid)
    for _ in range(angle):
        rotated_grid = []
        for col in range(len(grid[0]) - 1, -1, -1):
            rotated_grid.append([row[col] for row in grid])
        grid = rotated_grid
    return grid


def flip_h(grid):
    """flip horizontally"""
    grid = deepcopy(grid)
    for i in range(len(grid)):
        grid[i] = list(reversed(grid[i]))
    return grid


def flip_v(grid):
    """flip vertically"""
    grid = deepcopy(grid)
    for i in range(len(grid) // 2):
        grid[i], grid[~i] = grid[~i], grid[i]
    return grid


def stringify(ll):
    ll = [''.join(l) for l in ll]
    return '-'.join(ll)

from collections import Counter, defaultdict
def sol(grids: dict):
    up = defaultdict(list)
    # grids = {'a': [['.', '.', '.', '#', '.'],
    #                ['.', '.', '.', '.', '.'],
    #                ['#', '.', '#', '.', '.'],
    #                ['.', '.', '.', '.', '#'],
    #                ['#', '#', '.', '.', '#']]}
    for name, grid in grids.items():
        for angle in range(4):
            rgrid = rotate_left(grid, angle)
            up[''.join(rgrid[0])].append(name)

            rhgrid = flip_h(rgrid)
            up[''.join(rhgrid[0])].append(name)

    up = {key: tuple(sorted(val)) for key, val in up.items()}

    print(len(up))
    print(Counter(up.values()))
    for k, c in up.items():
        print(k, c)

    # print(len(gdict))
    # print(Counter(gdict.values()))
    # for k, c in gdict.items():
    #     print(k, c)


if __name__ == "__main__":
    sol(parse_input(sys.argv[1]))


