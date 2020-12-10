#!/usr/bin/env python3

import fileinput


def sol(lines):
    cnt = 0
    must_have_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    fields = set()
    for idx, line in enumerate(lines):
        if line != '':
            for s in line.split():
                k, v = s.split(':')
                fields.add(k)
        if line == '' or idx == len(lines) - 1:
            cnt += must_have_fields.issubset(fields)
            fields = set()
    print(cnt)



if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)

