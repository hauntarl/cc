"""
[Easy] https://cses.fi/problemset/task/1643
[Solution] https://cses.fi/paste/a5b242df4f454ae84c6bfe/

Given an array of n integers, your task is to find the maximum sum of values in
a contiguous, nonempty subarray.

The first input line has an integer n: the size of the array.

The second line has n integers x1,x2,…,xn: the array values.

Print one integer: the maximum subarray sum.

Constraints:
1 ≤ n ≤ 2⋅10^5
-10^9 ≤ xi ≤ 10^9

Input:
8
-1 3 -2 5 3 -5 2 2

Output:
9
"""
from util import timeit

MIN = -10**9 - 1


@timeit
def maximum_subarray_sum(nums: list[int]) -> int:
    """
    Kadane's Algorithm

    The idea is to calculate, for each array position, the maximum sum of a 
    subarray that ends at that position. After this, the answer for the problem 
    is the maximum of those sums.

    Refer: https://github.com/hauntarl/cc/blob/main/max_subarray_sum.py, for
    more details
    """
    best, curr = MIN, MIN
    for n in nums:
        curr = max(n, curr + n)
        best = max(best, curr)
    return best


if __name__ == '__main__':
    from collections import namedtuple

    Test = namedtuple('Test', ['inp', 'exp'])
    cases = [
        Test([-1, 3, -2, 5, 3, -5, 2, 2], 9),
        Test([1] * 10, 10),
        Test([-1] * 10, -1),
        Test([24, 7, -27, 17, -67, 65, -23, 58, 85, -39], 185),
        Test([99, -59, 31, 83, -79, 64, -20, -87, 40, -31], 154),
        Test([-19, 61, 60, 33, 67, 19, -8, 92, 59, -37], 383),
        Test([-1, -1, -1, -1, -2], -1),
        Test([-2, -3], -2),
    ]

    for tc in cases:
        assert (maximum_subarray_sum(tc.inp) == tc.exp)
