#!/usr/bin/env python3

"""Template for AOC python scripts"""


import fileinput
import sys


def parse_input(filepath):
    grids = {}
    with open(filepath, 'r') as file:
        ss = file.read()
        for chunk in ss[:-1].split('\n\n'):
            lines = [l.strip() for l in chunk.split('\n')]
            name = lines[0].split()[1][:-1]
            grids[int(name)] = lines[1:]

    return grids


def sol(grids: dict):
    edges = {}
    free_edges = {}
    for name, grid in grids.items():
        upper_edge = grid[0]
        lower_edge = grid[-1]
        left_edge = [l[0] for l in grid]
        right_edge = [l[-1] for l in grid]

        for edge in [upper_edge, lower_edge, right_edge, left_edge]:
            se = ''.join(edge)
            rse = ''.join(reversed(edge))
            if se in free_edges:
                free_edges.pop(se)
            elif rse in free_edges:
                free_edges.pop(rse)
            else:
                free_edges[se] = name

    d = {}
    for e, name in free_edges.items():
        d.setdefault(name, []).append(e)

    res = 1
    for name in d:
        if len(d[name]) > 1:
            res *= name

    print(res)


if __name__ == "__main__":
    sol(parse_input(sys.argv[1]))
