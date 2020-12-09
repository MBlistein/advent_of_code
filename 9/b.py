#!/usr/bin/env python3

"""Find the sliding window with sum == TARGET; return the sum of it's min and
max elements"""


import fileinput


TARGET = 177777905


def sol(lines):
    nums = list(map(int, lines))
    left = cursum = 0
    for right in range(len(nums)):
        cursum += nums[right]
        while cursum > TARGET:
            cursum -= nums[left]
            left += 1
        if cursum == TARGET and left < right:
            print(min(nums[left: right+1]) + max(nums[left: right+1]))
            return



if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
