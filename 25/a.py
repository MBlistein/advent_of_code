#!/usr/bin/env python3

"""Hack door by knowing the key generator's prime"""


import fileinput


MOD = 20201227


def sol(lines):
    card_pub, door_pub = map(int, lines)
    card_cycles = find_num_cycles(card_pub)
    print(encrypt(door_pub, card_cycles))


def find_num_cycles(public_key):
    num = 1
    num_cycles = 0
    while num != public_key:
        num_cycles += 1
        num *= 7
        num %= MOD
    return num_cycles


def encrypt(subject_num, num_cycles):
    num = 1
    for _ in range(num_cycles):
        num *= subject_num
        num %= MOD
    return num


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
