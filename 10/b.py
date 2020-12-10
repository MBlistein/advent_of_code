#!/usr/bin/env python3

"""Top-down and bottom-up dp solutions, considering duplicate adapters.
Both are O(n) time and space"""


import fileinput
from functools import lru_cache


def sol(lines):
    adapters = [int(a) for a in lines]
    built_in = max(adapters) + 3
    adapters += [0, built_in]  # add socket and built-in
    adapters.sort()

    top_down_dp(adapters)
    bottom_up_dp(adapters)


def top_down_dp(adapters):
    @lru_cache(None)
    def backtrack(idx):
        if idx == len(adapters) - 1:
            return 1  # sucessful connections

        cnt = 0
        j = idx + 1
        while j < len(adapters) and adapters[idx] + 3 >= adapters[j]:
            cnt += backtrack(j)
            j += 1
        return cnt

    print(backtrack(0))


def bottom_up_dp(adapters):
    n = len(adapters)
    dp = [0] * (n-1) + [1]

    for idx in range(n-1, -1, -1):
        j = idx + 1
        while j < n and adapters[idx] + 3 >= adapters[j]:
            dp[idx] += dp[j]
            j += 1
    print(dp[0])


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)

