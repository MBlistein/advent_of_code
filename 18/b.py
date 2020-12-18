#!/usr/bin/env python3

"""Main ideas:
    * Evaluate parentheses recursively
    * Addition has higher precedence than multiplication --> compress each
      addition sequence into a term 'consecutive_sum'
"""


import fileinput


def eval_expr(s, idx, n):
    sidx = idx
    res = 1
    consecutive_sum = num = 0
    while idx < n:
        if s[idx].isdigit():
            num = num * 10 + int(s[idx])
            idx += 1
        elif s[idx] == '(':
            num, idx = eval_expr(s, idx+1, n)
        elif s[idx] == '+':
            consecutive_sum += num
            num = 0
            idx += 1
        elif s[idx] == '*':
            res *= consecutive_sum + num
            consecutive_sum = num = 0
            idx += 1
        elif s[idx] == ')':
            res *= consecutive_sum + num
            idx += 1
            break

        if idx == n:
            res *= consecutive_sum + num

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

    print("Overall sum:", res)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
