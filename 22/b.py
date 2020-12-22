#!/usr/bin/env python3

"""Template for AOC python scripts"""


import fileinput
from collections import deque
from itertools import islice
from typing import Tuple


def update_win_p1(cards1, cards2):
        cards1.append(cards1.popleft())
        cards1.append(cards2.popleft())


def update_win_p2(cards1, cards2):
        cards2.append(cards2.popleft())
        cards2.append(cards1.popleft())


def game_a(cards1: deque, cards2: deque) -> Tuple[deque]:
    while cards1 and cards2:
        update_win_p1(cards1, cards2) if cards1[0] > cards2[0] else update_win_p2(cards1, cards2)
    return cards1, cards2


def game_b(cards1: deque, cards2: deque) -> Tuple[deque]:
    seen = set()
    while cards1 and cards2:
        if tuple(cards1) in seen:
            return cards1, []  # player 1 wins
        seen.add(tuple(cards1))

        if cards1[0] < len(cards1) and cards2[0] < len(cards2):
            p1, p2 = game_b(deque(islice(cards1, 1, cards1[0] + 1)),
                            deque(islice(cards2, 1, cards2[0] + 1)))
        else:
            p1, p2 = cards1[0] > cards2[0], cards2[0] > cards1[0]

        update_win_p1(cards1, cards2) if p1 else update_win_p2(cards1, cards2)

    return cards1, cards2


def calc_winning_score(cards):
    res = 0
    for i in range(len(cards)):
        res += (i + 1) * cards[~i]
    return res


def sol(lines):
    cards = []
    for line in lines:
        if line and line[0].isdigit():
            cards.append(int(line))
    assert len(cards) == len(set(cards))  # logic relies on unique cards
    assert min(cards) > 0                 # logic relies on cards > 0

    a1, a2 = game_a(deque(cards[: len(cards)//2]), deque(cards[len(cards)//2: ]))
    print('part A:', calc_winning_score(a1 if a1 else a2))

    b1, b2 = game_b(deque(cards[: len(cards)//2]), deque(cards[len(cards)//2: ]))
    print('part B:', calc_winning_score(b1 if b1 else b2))


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
