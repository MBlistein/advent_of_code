#!/usr/bin/env python3

"""Handle bit clearing and setting separately for clean code"""


import fileinput


def sol(lines):
    mem = {}
    cle_mask = 0  # used to swap '1'-bits to '0'
    set_mask = 0  # used to swap '0'-bits to '1'
    for l in lines:
        if l[:3] == 'mem':
            address = int(l.split()[0][4:-1])
            val = int(l.split()[-1])
            val &= cle_mask
            val |= set_mask
            mem[address] = val
        else:
            mask = l.split()[-1]
            cle_mask = int(''.join(['0' if c == '0' else '1' for c in mask]), 2)
            set_mask = int(''.join(['1' if c == '1' else '0' for c in mask]), 2)

    print(sum(mem.values()))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
