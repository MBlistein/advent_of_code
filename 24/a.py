#!/usr/bin/env python3

"""part A: grid navigation in hexagonal grid
   part B: BFS in hexagonal grid"""


import fileinput
from collections import deque
from typing import Dict, List, Tuple


def get_directions(lines: List[str]) -> List[List[str]]:
    directions = []
    for line in lines:
        ld = []
        n = len(line)
        idx = 0
        while idx < n:
            if line[idx] in 'ew':
                ld.append(line[idx])
                idx += 1
            elif line[idx] in 'sn':
                if idx < n - 1 and line[idx + 1] in 'ew':
                    ld.append(line[idx: idx + 2])
                    idx += 2
                else:
                    ld.append(line[idx])
                    idx += 1
        directions.append(ld)
    return directions


def lay_tiles(directions: List[List[str]]) -> Dict[(Tuple[int], int)]:
    seen = {}
    for dirs in directions:
        x, y = 0, 0
        for d in dirs:
            if d == 'ne':
                x += 1
                y += 2
            elif d == 'e':
                x += 2
            elif d == 'se':
                x += 1
                y -= 2
            elif d == 'sw':
                x -= 1
                y -= 2
            elif d == 'w':
                x -= 2
            elif d == 'nw':
                x -= 1
                y += 2
            else:
                raise ValueError('b')

        if (x, y) in seen:
            seen[(x, y)] ^= 1
        else:
            seen[(x, y)] = 1  # black
    return seen


def flip_tiles(prev: Dict[(Tuple[int], int)]) -> Dict[(Tuple[int], int)]:
    """BFS from the center tile: flip tiles according to rules:
        * any black tile that does not have exactly 1 or 2 black neighbors
        * any white tile that has exactly two black neighbors
    """
    new = {}
    q = deque([(0, 0)])
    while q:
        ux, uy = q.popleft()
        black_count = 0
        for vx, vy in [(ux + 1, uy + 2), (ux + 2, uy), (ux + 1, uy -2),
                       (ux - 1, uy - 2), (ux - 2, uy), (ux - 1, uy + 2)]:
            if prev.get((vx, vy), 0) == 1:
                black_count += 1

            if (vx, vy) not in new and ((vx, vy) in prev or prev.get((ux, uy), 0) == 1):
                # include previously unknown white tiles bordering black tiles
                new[(vx, vy)] = prev.get((vy, vy), 0)
                q.append((vx, vy))

        if prev.get((ux, uy), 0) == 1 and not 1 <= black_count <= 2:
            new[(ux, uy)] = 0
        elif prev.get((ux, uy), 0) == 0 and black_count == 2:
            new[(ux, uy)] = 1
        else:
            new[(ux, uy)] = prev.get((ux, uy), 0)

    return new


def sol(lines: List[str]) -> None:
    directions = get_directions(lines)
    tile_state = lay_tiles(directions)
    print('part A:', sum(tile_state.values()))

    for day in range(100):
        tile_state = flip_tiles(tile_state)
    print('part B:', sum(tile_state.values()))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
