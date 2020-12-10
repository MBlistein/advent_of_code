#!/usr/bin/env python3

"""Part 1
Find loop via dfs"""


import fileinput


def sol(lines):
    idx = acc = 0
    seen = set()

    def dfs(idx, acc):
        if idx in seen:
            print(acc)
            return

        seen.add(idx)
        op, num = lines[idx].split()
        if op == 'acc':
            return dfs(idx + 1, acc + int(num))
        elif op == 'nop':
            return dfs(idx+1, acc)
        else:
            return dfs(idx + int(num), acc)

    dfs(0, 0)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
