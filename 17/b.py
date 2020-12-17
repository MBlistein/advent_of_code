#!/usr/bin/env python3

"""Template for AOC python scripts"""


import copy
import fileinput


def num_occupied(hypercube, grid, layer, row, col):
    num_occ = 0
    for g in range(grid - 1, grid + 2):
        for l in range(layer - 1, layer + 2):
            for r in range(row-1, row + 2):
                for c in range(col-1, col + 2):
                    if g == grid and l == layer and r == row and c == col:
                        continue
                    if hypercube[g][l][r][c] == '#':
                        num_occ += 1
    return num_occ


def sol(lines):
    init_layer = []
    for line in lines:
        init_layer.append(list(line))

    debug = False
    num_cycles = 6
    buffer = num_cycles + 1

    num_rows = len(init_layer)
    num_cols = len(init_layer[0])
    final_rows = num_rows + 2 * buffer
    final_cols = num_cols + 2 * buffer
    num_layers = 1 + 2 * buffer
    num_grids = 1 + 2 * buffer

    grid = []
    for idx in range(num_layers):
        grid.append([['.'] * final_cols for _ in range(final_rows)])

    hypercube = [copy.deepcopy(grid) for _ in range(num_grids)]

    for r in range(num_rows):
        for c in range(num_cols):
            hypercube[buffer][buffer][buffer + r][buffer + c] = init_layer[r][c]

    debug_print(debug, hypercube)

    for _ in range(num_cycles):
        new = copy.deepcopy(hypercube)
        if debug:
            print()
            print('########################')
        for g in range(1, num_grids-1):
            for l in range(1, num_layers-1):
                for r in range(1, final_rows-1):
                    for c in range(1, final_cols-1):
                        num_occ = num_occupied(hypercube, g, l, r, c)
                        if hypercube[g][l][r][c] == '#' and not (2 <= num_occ <= 3):
                            new[g][l][r][c] = '.'
                        elif hypercube[g][l][r][c] == '.' and num_occ == 3:
                            new[g][l][r][c] = '#'
        hypercube = new
        debug_print(debug, hypercube)


    tot_active = 0
    for g in range(1, num_grids-1):
        for l in range(1, num_layers-1):
            for r in range(1, final_rows-1):
                for c in range(1, final_cols-1):
                    if hypercube[g][l][r][c] == '#':
                        tot_active += 1
    print(tot_active)


def debug_print(debug, hypercube):
    if not debug:
        return

    num_grids = len(hypercube)
    num_layers = len(hypercube[0])
    for g, grid in enumerate(hypercube):
        for l, layer in enumerate(grid):
            print()
            print(f"z = {g - num_grids // 2}, w = {l - num_layers // 2}")
            for r in layer:
                print(''.join(r))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
