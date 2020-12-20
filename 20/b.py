#!/usr/bin/env python3

"""Template for AOC python scripts"""


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


def find_corner_piece(grids):
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

    corner_piece = non_matching_edges = None
    for name in d:
        if len(d[name]) > 1:
            corner_piece, non_matching_edges = name, d[name]
            break
    return corner_piece, non_matching_edges


def build_single_image(grids, start_corner, outside_edges):
    image = grids.pop(start_corner)
    # make this the upper left piece for easier processing
    upper_edge = ''.join(image[0])
    lower_edge = ''.join(image[-1])
    left_edge = ''.join([l[0] for l in image])
    right_edge = ''.join([l[-1] for l in image])
    if set(outside_edges) == set([upper_edge, right_edge]):
        image = rotate_left(image, 1)
    elif set(outside_edges) == set([lower_edge, right_edge]):
        image = rotate_left(image, 2)
    elif set(outside_edges) == set([lower_edge, left_edge]):
        image = rotate_left(image, 3)

    # free edges consist exclusively of right edges
    free_right_edges = {''.join([l[-1] for l in image]): (0, 0)}
    free_lower_edges = {''.join(image[-1]): (0, 0)}

    # process
    while grids:
        match = False
        for name, tile in grids.items():
            for angle in range(4):
                if match:
                    break
                r_tile = rotate_left(tile, angle)
                fhr_tile = flip_h(r_tile)

                upper_edge = ''.join(r_tile[0])
                left_edge = ''.join([l[0] for l in r_tile])
                lower_edge = ''.join(r_tile[-1])
                right_edge = ''.join([l[-1] for l in r_tile])
                f_upper_edge = ''.join(reversed(upper_edge))
                f_lower_edge = ''.join(reversed(lower_edge))

                # try to match above
                if upper_edge in free_lower_edges:
                    match = True
                    upper_pos = free_lower_edges.pop(upper_edge)
                    new_pos = upper_pos[0] + 1, upper_pos[1]

                    free_lower_edges[lower_edge] = new_pos
                    free_right_edges[right_edge] = new_pos
                    image = update_image(image, r_tile, new_pos)

                elif f_upper_edge in free_lower_edges:
                    match = True
                    upper_pos = free_lower_edges.pop(f_upper_edge)
                    new_pos = upper_pos[0] + 1, upper_pos[1]

                    free_lower_edges[f_lower_edge] = new_pos
                    free_right_edges[left_edge] = new_pos
                    image = update_image(image, fhr_tile, new_pos)

                # try to match left
                elif left_edge in free_right_edges:
                    match = True
                    left_pos = free_right_edges.pop(left_edge)
                    new_pos = left_pos[0], left_pos[1] + 1

                    free_lower_edges[lower_edge] = new_pos
                    free_right_edges[right_edge] = new_pos
                    image = update_image(image, r_tile, new_pos)

                elif right_edge in free_right_edges:
                    match = True
                    left_pos = free_right_edges.pop(right_edge)
                    new_pos = left_pos[0], left_pos[1] + 1

                    free_lower_edges[f_lower_edge] = new_pos
                    free_right_edges[left_edge] = new_pos
                    image = update_image(image, fhr_tile, new_pos)
            if match:
                break
        if match:
            grids.pop(name)
    return image


def update_image(image, tile, pos):
    l = len(tile)
    row, col = pos[0] * l, pos[1] * l
    if len(image) - 1 < row:
        for _ in range(l):
            image.append([])

    for dr in range(l):
        if len(image[row + dr]) - 1 <= col:
            image[row + dr] += ['.'] * (col - len(image[row + dr]))
            image[row + dr] += (tile[dr])
        elif len(image[row + dr]) >= col + l:
            for dc in range(l):
                image[row + dr][col + dc] = tile[dr][dc]

    return image


def clean_image(image, tile_size):
    clean_image = []
    for idx in range(0, len(image), 10):
        clean_image += image[idx + 1: idx + 9]

    for idx, row in enumerate(clean_image):
        clean_row = []
        for j in range(0, len(row), 10):
            clean_row += row[j+1: j + 9]
        clean_image[idx] = clean_row

    return clean_image


def check_monster(image):
    num_monsters = 0
    n = len(image)
    SEA_MONSTER = ['..................#.',
                   '#....##....##....###',
                   '.#..#..#..#..#..#...']
    s = len(SEA_MONSTER[0])

    for r in range(n-2):
        for c in range(n-s):
            found_monster = True
            for dr in range(3):
                if not found_monster:
                    break
                for dc in range(s):
                    if SEA_MONSTER[dr][dc] == '#' and image[r + dr][c + dc] != '#':
                        found_monster = False
                        break
            if found_monster:
                num_monsters += 1
                for dr in range(3):
                    for dc in range(s):
                        if SEA_MONSTER[dr][dc] == '#' and image[r + dr][c + dc] == '#':
                            image[r + dr][c + dc] = 'O'

    return num_monsters


def count_tags(image):
    cnt = 0
    for row in image:
        cnt += row.count('#')
    return cnt


def sol(grids: dict):
    start_corner, outside_edges = find_corner_piece(grids)
    image = build_single_image(grids, start_corner, outside_edges)
    image = clean_image(image, 10)

    for r in image:
        print(''.join(r))

    for angle in range(4):
        for flip in (0, 1):
            new_image = rotate_left(image, angle)
            if flip:
                new_image = flip_h(new_image)

            num_monsters = check_monster(new_image)
            print(f'Found {num_monsters} monsters')
            if num_monsters > 0:
                for r in new_image:
                    print(''.join(r))
                print(count_tags(new_image))
                return


def test_grid_manip():
    grid = [['.', '.', '#', '#', '.'],
            ['#', '.', '.', '.', '.'],
            ['.', '.', '#', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '#', '.', '.', '#']]

    for a in range(0, 4):
        print()
        print("angle: ", a)
        gr = rotate_left(deepcopy(grid), a)
        for r in gr:
            print(''.join(r))

        print('\nflipped rotation:')
        gf = flip_h(gr)
        for r in gr:
            print(''.join(r))


if __name__ == "__main__":
    sol(parse_input(sys.argv[1]))


