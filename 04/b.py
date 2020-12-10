#!/usr/bin/env python3

import fileinput


def sol(lines):
    cnt = 0
    must_have_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    fields = set()
    for i, line in enumerate(lines):
        if line != '':
            for s in line.split():
                k, v = s.split(':')
                if k == 'byr':
                    if not 1920 <= int(v) <= 2002:
                        continue
                elif k == 'iyr':
                    if not 2010 <= int(v) <= 2020:
                        continue
                elif k == 'eyr':
                    if not 2020 <= int(v) <= 2030:
                        continue
                elif k == 'hgt':
                    if len(v) >= 2 and v[-2:] == 'cm':
                        if not 150 <= int(v[:-2]) <= 193:
                            continue
                    elif len(v) >= 2 and v[-2:] == 'in':
                        if not 59 <= int(v[:-2]) <= 76:
                            continue
                    else:
                        continue
                elif k == 'hcl':
                    if not (v[0] == '#' and len(v[1:]) == 6 and v[1:].isalnum()):
                        continue
                elif k == 'ecl':
                    if not v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        continue
                elif k == 'pid':
                    if not (len(v) == 9 and v.isnumeric()):
                        continue
                fields.add(k)
        if line == '' or i == len(lines) - 1:
            cnt += must_have_fields.issubset(fields)
            fields = set()

    print(cnt)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)

