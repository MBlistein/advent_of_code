#!/usr/bin/env python3

"""Evaluate parentheses recursively"""


import fileinput


def eval_expr(s, idx, n):
    sidx = idx
    res = 0
    num = 0
    op = '+'
    while idx < n:
        if s[idx].isdigit():
            num = num * 10 + int(s[idx])
            idx += 1
        elif s[idx] == '(':
            num, idx = eval_expr(s, idx+1, n)

        if idx == n or s[idx] in '+*)':
            if op == '+':
                res += num
            elif op == '*':
                res *= num
            num = 0

            if idx < n:
                op = s[idx]
                idx += 1
                if op == ')':
                    break
    print(f"{s[max(0, sidx-1): idx]} = {res}")

    return res, idx


def sol(lines):
    res = 0
    for line in lines:
        print('\n', line)
        line = line.replace(' ', '')
        lres, _ = eval_expr(line, 0, len(line))
        print(lres)
        res += lres

    print(res)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
