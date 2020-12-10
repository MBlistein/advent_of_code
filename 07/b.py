#!/usr/bin/env python3

"""Template for AOC python scripts"""


import fileinput
from functools import lru_cache


def sol(lines):
    graph = {}  # {inside_bag: {outside_bag: capacity}}
    for l in lines:
        outside_bag, contained_bags = l.split('contain')
        u = ''.join(outside_bag.split()[: -1])

        contained_bags = contained_bags.split(',')
        for bag in contained_bags:
            info = bag.split()
            amnt = info[0]
            v = ''.join(info[1:-1])  # removes 'bag'
            if amnt != 'no':
                graph.setdefault(u, {})[v] = int(amnt)

    @lru_cache(None)
    def dfs(u):
        """Count the number of bags contained in u, as well as u itsef"""
        cnt = 1  # count current bag
        for v, amnt in graph.get(u, {}).items():
            cnt += amnt * dfs(v)
        return cnt

    print(dfs('shinygold') - 1)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
