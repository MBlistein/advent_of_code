#!/usr/bin/env python3

"""Part 2
We may swap exactly one 'jmp' for a 'nop' or vice versa.
Idea: try to swap the jmp/ nop encountered last before hitting a loop.
If that does not work, backtrack further up the chain

Note that nodes are not removed from 'seen' when backtracking. We can do this
because we only ever modify the field we currently stand on --> if a field
leads to a cycle once, it will always lead to a cycle.
This improves Time complexity from O(n**2) to O(n)."""


import fileinput


def sol(lines):
    seen = set()
    n = len(lines)

    def backtrack(idx, acc, retries):
        if idx in seen:
            return None  # found loop
        elif idx == n:
            return acc

        seen.add(idx)
        op, num = lines[idx].split()
        val = int(num)
        if op == 'acc':
            res = backtrack(idx + 1, acc + val, retries)
            return res
        elif op == 'nop':
            res = backtrack(idx+1, acc, retries)
            if res is None and retries == 1:
                res = backtrack(idx + val, acc, 0)  # try to change 'nop' to 'jmp'
            return res
        elif op == 'jmp':
            res = backtrack(idx + val, acc, retries)
            if res is None and retries == 1:
                res = backtrack(idx + 1, acc, 0)  # try to change 'jmp' to 'nop'
            return res
        else:
            raise ValueError(f"Invalid instruction {lines[idx]}")

    print(backtrack(0, 0, 1))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
