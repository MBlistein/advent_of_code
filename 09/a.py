#!/usr/bin/env python3

"""Two-sum on sliding window"""


import fileinput


def two_sum(nums, left, right, target):
    mem = set()
    for num in nums[left: right+1]:
        if target - num in mem:
            return True
        mem.add(num)
    return False


def sol(lines):
    nums = list(map(int, lines))
    for idx in range(25, len(lines)):
        if not two_sum(nums, idx-25, idx-1, nums[idx]):
            print(nums[idx])
            return



if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
