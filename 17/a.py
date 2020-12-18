#!/usr/bin/env python3

"""Template for AOC python scripts"""


import copy
import fileinput


def num_occupied(grid, layer, row, col):
    num_occ = 0
    for l in range(layer - 1, layer + 2):
        for r in range(row-1, row + 2):
            for c in range(col-1, col + 2):
                if l == layer and r == row and c == col:
                    continue
                if grid[l][r][c] == '#':
                    num_occ += 1
    return num_occ


def sol(lines, debug):
    grid = []
    init_layer = []
    for line in lines:
        init_layer.append(list(line))

    num_cycles = 6
    buffer = num_cycles + 1

    num_rows = len(init_layer)
    num_cols = len(init_layer[0])
    final_rows = num_rows + 2 * buffer
    final_cols = num_cols + 2 * buffer
    num_layers = 1 + 2 * buffer
    for idx in range(num_layers):
        grid.append([['.'] * final_cols for _ in range(final_rows)])

    for r in range(num_rows):
        for c in range(num_cols):
            grid[buffer][buffer + r][buffer + c] = init_layer[r][c]

    if debug:
        for l in grid:
            print()
            for r in l:
                print(''.join(r))

    for _ in range(num_cycles):
        if debug:
            print('\n########################')
        new = copy.deepcopy(grid)
        for l in range(1, num_layers-1):
            for r in range(1, final_rows-1):
                for c in range(1, final_cols-1):
                    num_occ = num_occupied(grid, l, r, c)
                    if grid[l][r][c] == '#' and not (2 <= num_occ <= 3):
                        new[l][r][c] = '.'
                    elif grid[l][r][c] == '.' and num_occ == 3:
                        new[l][r][c] = '#'
        grid = new
        if debug:
            for l in grid:
                print()
                for r in l:
                    print(''.join(r))

    tot_active = 0
    for l in range(num_layers):
        for r in range(final_rows):
            for c in range(final_cols):
                if grid[l][r][c] == '#':
                    tot_active += 1
    print(tot_active)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines, False)
