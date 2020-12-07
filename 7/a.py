#!/usr/bin/env python3

"""
The bag dependencies can be modeled as a directed graph.
"""


import fileinput


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
                graph.setdefault(v, {})[u] = int(amnt)

    def dfs(u):
        """Count the number of bags that could contain u, including u"""
        if u in seen:
            return 0

        seen.add(u)
        cnt = 1  # count current bag
        for v in graph.get(u, {}):
            cnt += dfs(v)
        return cnt

    seen = set()  # count unique bags
    print(dfs('shinygold') - 1)
    print(len(seen) - 1)  # same as line above



if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
