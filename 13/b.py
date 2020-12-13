#!/usr/bin/env python3

""" Task: find the time T where (T + offset) % duration == 0 for all busses
Intuition: Imagine several sign curves in the same plot, each of which are
           phase-shifted by a negative offset 0. At what time T will they all
           simultaneously traverse the x axis?
Solution:
1) find the earliest time t12 for the first two busses by either:
     * Brute force calculation
     * Via the multiplicative inverse of duration1 mod duration2
2) All bus durations d_i are prime numbers --> for any subset of buses, there is
   no lower common multiple than their product.
   This means: the next valid timestamps for buses 1 and 2 are:
   t12 + D, t12 + 2*D, t12 + 3*dp, ..., where D = d_1 * d_2
   Therfore: update the step length in the BF calculation to d_1 * d_2
3) Since the first meeting point of buses 1 and 2 is fixed, we have to take it
   as offset when searching for further matches --> update start_time to t12
4-n) Repeat steps 1 - 3 for the rest of the buses
"""


import fileinput


def find_first_match(T, z, p, offset):
    while True:
        T += z
        if (T + offset) % p == 0:
            return T


def sol(lines):
    buses = []
    for idx, duration in enumerate(lines[1].split(',')):
        if duration != 'x':
            buses.append((idx, int(duration)))  # offset, duration

    d1 = buses[0][1]
    T = 0  # T + offset_i = 0 mod duration_i for all previous buses
    for offset, d2 in buses[1:]:
        T = find_first_match(T, d1, d2, offset)
        d1 *= d2  # prime numbers --> lcm is product
    print(T)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
