#!/usr/bin/env python3

"""Generate 2**x setting and clearing bitmasks, where x = mask.count('X').
Then reuse bit clearing/ setting logic from part A."""


import fileinput
from typing import List


def sol(lines: List[str]) -> None:
    mem = {}
    cle_masks, set_masks = [], []
    for l in lines:
        if l[:3] == 'mem':
            address = int(l.split()[0][4:-1])
            val = int(l.split()[-1])

            for idx in range(len(cle_masks)):
                masked_address = address & cle_masks[idx]
                masked_address |= set_masks[idx]
                mem[masked_address] = val
        else:
            mask = l.split()[-1]
            cle_masks = [0]
            set_masks = [0]
            for idx in range(len(mask)):
                for j in range(len(cle_masks)):
                    cle_masks[j] <<= 1
                    cle_masks[j] |= 1  # if X: don't clear
                    set_masks[j] <<= 1
                    set_masks[j] |= 0 if mask[idx] == '0' else 1  # if X: do set

                if mask[idx] == 'X':
                    for k in range(len(cle_masks)):
                        cle_masks.append(cle_masks[k] & ~1)  # do clear
                        set_masks.append(set_masks[k] & ~1)  # don't set

    print(sum(mem.values()))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
