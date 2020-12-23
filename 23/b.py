#!/usr/bin/env python3

"""Template for AOC python scripts"""


import fileinput


N = int(input())


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


def sol(lines):
    cnt = 1
    nodes = {}
    numbers = list(map(int, lines[0]))
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

    startnode = nodes[numbers[0]]
    for _ in range(N):
        # if cnt % 1000 == 0:
        #     print(cnt)
        # cnt += 1
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


def rotate(L, start_idx):
    """make start element first element in list --> process --> rotate back"""
    n = len(L)
    new = L[start_idx:] + L[:start_idx]
    nxt_smaller = new[0] - 1
    if nxt_smaller == 0:
        nxt_smaller = 9
    print('new:', new)

    removed = new[1: 4]
    new = [new[0]] + new[4:]
    print('cut:', new)

    for _ in range(3):
        if nxt_smaller in removed:
            nxt_smaller -= 1
            if nxt_smaller == 0:
                nxt_smaller = 9

    for kdx in range(1, len(new)):
        if new[kdx] == nxt_smaller:
            new = new[:kdx + 1] + removed + new[kdx + 1: ]
            print(f'insert at idx {kdx}')
            break
        else:
            print(f'{new}[{kdx}] = {new[kdx]} != {nxt_smaller}')
    print('ins:', new)

    return new[-start_idx:] + new[: -start_idx]  # rotate back


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
