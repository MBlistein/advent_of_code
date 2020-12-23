#!/usr/bin/env python3

"""Brute force: Use circular doubly linked list to simulate each move in O(1)"""


import fileinput
from typing import List, Tuple


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def remove_next_3(node):
    removed_head = removed_tail = node.next
    for _ in range(2):
        removed_tail = removed_tail.next

    node.next = removed_tail.next
    removed_tail.next.prev = node

    removed_head.prev = removed_tail.next = None
    return removed_head


def insert_after(node, sublist_head):
    right = node.next

    node.next = sublist_head
    sublist_head.prev = node

    sublist_tail = sublist_head
    while sublist_tail.next:
        sublist_tail = sublist_tail.next

    sublist_tail.next = right
    right.prev = sublist_tail


def construct_dll(numbers: List[int]) -> dict:
    """Creates a doubly linked list, returns a dict mapping keys to nodes"""
    nodes = {}
    for idx, num in enumerate(numbers):
        node = Node(num)
        if idx > 0:
            prevnode = nodes[numbers[idx-1]]
            node.prev = prevnode
            prevnode.next = node
        nodes[num] = node

    node10 = Node(10)
    node10.prev = nodes[numbers[-1]]
    nodes[numbers[-1]].next = node10
    nodes[10] = node10

    for num in range(11, 1000000):
        node = Node(num)
        node.prev = nodes[num-1]
        nodes[num-1].next = node
        nodes[num] = node

    nodeM = Node(1000000)
    nodeM.next = nodes[numbers[0]]
    nodes[numbers[0]].prev = nodeM
    nodeM.prev = nodes[999999]
    nodes[999999].next = nodeM
    nodes[1000000] = nodeM

    return nodes


def sol(lines):
    numbers = list(map(int, lines[0]))
    N = int(input("Number of moves: "))
    nodes = construct_dll(numbers)

    startnode = nodes[numbers[0]]
    for _ in range(N):
        sublist_head = remove_next_3(startnode)

        removed_vals = []
        a = sublist_head
        while a:
            removed_vals.append(a.val)
            a = a.next

        nxt_smaller = startnode.val - 1
        if nxt_smaller == 0:
            nxt_smaller = 1000000
        for _ in range(3):
            if nxt_smaller in removed_vals:
                nxt_smaller -= 1
                if nxt_smaller == 0:
                    nxt_smaller = 1000000

        insert_after(nodes[nxt_smaller], sublist_head)
        startnode = startnode.next

    res = nodes[1].next.val * nodes[1].next.next.val
    print(nodes[1].next.val, nodes[1].next.next.val)
    print(res)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
