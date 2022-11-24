"""
[Easy] https://cses.fi/problemset/task/1074
[Solution] https://cses.fi/paste/a4051ed2e75150bd4c95cf/

There are n sticks with some lengths. Your task is to modify the sticks so that
each stick has the same length.

You can either lengthen and shorten each stick. Both operations cost x where x
is the difference between the new and original length.

What is the minimum total cost?

The first input line contains an integer n: the number of sticks.

Then there are n integers: p1,p2,…,pn: the lengths of the sticks.

Print one integer: the minimum total cost.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ pi ≤ 10^9

Input:
5
2 3 1 5 2

Output:
5
"""
from util import timeit
from random import randint


def three_way_partition(nums, beg, end, k):
    """
    Modified quick sort algorithm,
    Finds the kth smallest element in the given array.
    """
    if end - beg < 1:
        return nums[beg]

    pivot = nums[randint(beg, end - 1)]
    part1, part2, part3 = beg, beg, end - 1
    while part2 <= part3:
        if nums[part2] < pivot:
            nums[part1], nums[part2] = nums[part2], nums[part1]
            part1 += 1
            part2 += 1
        elif nums[part2] > pivot:
            nums[part3], nums[part2] = nums[part2], nums[part3]
            part3 -= 1
        else:
            part2 += 1

    if k - 1 < part1:
        return three_way_partition(nums, beg, part1, k)
    elif k - 1 > part3:
        return three_way_partition(nums, part3 + 1, end, k)
    else:
        return nums[part1]


@timeit
def stick_lengths(nums: list[int]) -> int:
    """
    Find the mid element in given array,
    Add up the absolute difference as cost.
    """
    mid = len(nums) // 2
    if len(nums) & 1:
        mid += 1

    target, cost = three_way_partition(nums, 0, len(nums), mid), 0
    print(nums, target)
    for n in nums:
        cost += abs(target - n)
    return cost


if __name__ == '__main__':
    from collections import namedtuple

    Test = namedtuple('Test', ['inp', 'exp'])
    cases = [
        Test([2, 3, 1, 5, 2], 5),
        Test([1], 0),
        Test([1] * 10, 0),
        Test([int(v) for v in '1 4 7 8 10 3 2 5 6 9'.split()], 25),
        Test([int(v) for v in '1 2 3 4 5'.split()], 6),
    ]

    for tc in cases:
        assert (stick_lengths(tc.inp) == tc.exp)
