#!/usr/bin/env python3

"""Use symmetry to only calculate half of the cube"""


import copy
import fileinput


def num_active(grid, layer, row, col):
    """Count active cubes"""
    num_ac = 0
    for l in range(layer - 1, layer + 2):
        if not 0 <= l < len(grid):
            continue
        for r in range(row-1, row + 2):
            if not 0 <= r < len(grid[0]):
                continue
            for c in range(col-1, col + 2):
                if not 0 <= c < len(grid[0][0]):
                    continue
                if l == layer and r == row and c == col:
                    continue
                if r >= 0 and grid[l][r][c] == '#':
                    num_ac += 1 if not (layer == 0 and l == 1) else 2
    return num_ac


def sol(lines, debug):
    init_layer = []
    for line in lines:
        init_layer.append(list(line))

    num_cycles = 6
    num_rows = len(init_layer) + 2 * num_cycles
    num_cols = len(init_layer[0]) + 2 * num_cycles
    num_layers = 1 + num_cycles  # symmetry: walk into one direction

    grid = []
    for idx in range(num_layers):
        grid.append([['.'] * num_cols for _ in range(num_rows)])

    # set initial configuration
    for r in range(len(init_layer)):
        for c in range(len(init_layer[0])):
            grid[0][num_cycles + r][num_cycles + c] = init_layer[r][c]

    if debug:
        for l in grid:
            print()
            for r in l:
                print(''.join(r))

    for _ in range(num_cycles):
        if debug:
            print('\n########################')
        new = copy.deepcopy(grid)
        for l in range(num_layers):
            for r in range(num_rows):
                for c in range(num_cols):
                    num_ac = num_active(grid, l, r, c)
                    if grid[l][r][c] == '#' and not (2 <= num_ac <= 3):
                        new[l][r][c] = '.'
                    elif grid[l][r][c] == '.' and num_ac == 3:
                        new[l][r][c] = '#'
        grid = new
        if debug:
            for l in grid:
                print()
                for r in l:
                    print(''.join(r))

    tot_active = 0
    for l in range(num_layers):
        layer_cnt = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[l][r][c] == '#':
                    layer_cnt += 1
        tot_active += layer_cnt if l == 0 else 2 * layer_cnt
    print(tot_active)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines, False)
