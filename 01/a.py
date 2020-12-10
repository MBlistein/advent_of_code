#!/usr/bin/env python3

def get_nums():
    nums = []
    with open("in.txt") as text:
        for line in text:
            nums.append(int(line.strip('\n')))
    return nums

def two_sum():
    nums = get_nums()
    mem = set()
    for num in nums:
        a = 2020 - num
        if a in mem:
            print(num * a)
            return
        mem.add(num)

def two_sum_limits(sorted_nums, start, target):
    left, right = start, len(sorted_nums) - 1
    while left < right:
        s = sorted_nums[left] + sorted_nums[right]
        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return sorted_nums[left] * sorted_nums[right]
    return None

def three_sum():
    nums = get_nums()
    nums.sort()
    for idx in range(len(nums)):
        two = two_sum_limits(nums, idx+1, 2020 - nums[idx])
        if two is not None:
            print(nums[idx] * two)


if __name__ == "__main__":
    two_sum()
    three_sum()
