"""
[Medium] https://cses.fi/problemset/task/2216
[Solution] https://cses.fi/paste/ee5178bcfb17191a4ca2bb/
[Explanation] https://stackoverflow.com/a/67539174

You are given an array that contains each number between 1…n exactly once. Your
task is to collect the numbers from 1 to n in increasing order.

On each round, you go through the array from left to right and collect as many
numbers as possible. What will be the total number of rounds?

The first line has an integer n: the array size.

The next line has n integers x1,x2,…,xn: the numbers in the array.

Print one integer: the number of rounds.

Constraints:
1 ≤ n ≤ 2⋅10^5

Input:
5
4 2 1 5 3

Output:
3
"""
from util import timeit


@timeit
def collecting_numbers(nums: list[int]) -> int:
    nums = [0] + nums
    harr = [0] * len(nums)
    for i in range(1, len(nums)):
        harr[nums[i]] = i

    ans = 1
    for i in range(2, len(nums)):
        if harr[i] < harr[i - 1]:
            ans += 1

    return ans


if __name__ == '__main__':
    from collections import namedtuple

    Test = namedtuple('Test', ['inp', 'exp'])
    cases = [
        Test([int(v) for v in '4 2 1 5 3'.split()], 3),
    ]

    for tc in cases:
        assert (collecting_numbers(tc.inp) == tc.exp)
