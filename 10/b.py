#!/usr/bin/env python3

""""""


import fileinput
from functools import lru_cache


def sol(lines):
    adapters = [int(a) for a in lines]
    built_in = max(adapters) + 3
    adapters += [0, built_in]  # add socket and built-in
    adapters.sort()

    @lru_cache(None)
    def backtrack(idx):
        if adapters[idx] == built_in:
            return 1  # sucessful connections

        cnt = 0
        j = idx + 1
        while j < len(adapters) and adapters[idx] + 3 >= adapters[j]:
            cnt += backtrack(j)
            j += 1
        return cnt

    print(backtrack(0))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)

