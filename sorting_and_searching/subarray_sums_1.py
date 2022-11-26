"""
[Medium] https://cses.fi/problemset/task/1660
[Solution] https://cses.fi/paste/ab0e622df2940c024cb153/

Given an array of n positive integers, your task is to count the number of
subarrays having sum x.

The first input line has two integers n and x: the size of the array and the
target sum x.

The next line has n integers a1,a2,…,an: the contents of the array.

Print one integer: the required number of subarrays.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ x, ai ≤ 10^9

Input:
5 7
2 4 1 2 7

Output:
3
"""
from util import timeit


@timeit
def subarray_sums_1(nums: list[int], target: int) -> int:
    """
    Sliding window algorithm,
    . create two pointers, i and j for start and end of subarray respectively
    . iterate until the subarray size equals zero
    . if sum of current subarray equals the target
        . increment count
        . remove first element from the current subarray
    . if sum is greater than target
        . remove first element from the current subarray
    . if sum is greater than target
        . append the next element to the current subarray
        . if no next element present, break the loop
    """
    i, j, count, total = 0, 0, 0, 0
    while i <= j:
        if total < target:
            if j == len(nums):
                break

            total += nums[j]
            j += 1
            continue

        if total == target:
            count += 1
        total -= nums[i]
        i += 1

    return count


if __name__ == '__main__':
    from collections import namedtuple

    Test = namedtuple('Test', ['inp', 'exp'])
    cases = [
        Test(([int(v) for v in '2 4 1 2 7'.split()], 7), 3),
        Test(([int(v) for v in '2 4 1 2 7'.split()], 6), 1),
        Test(([int(v) for v in '2 4 1 2 7'.split()], 9), 2),
        Test(([int(v) for v in '1 1 1 1 1 1 1 1 3 4'.split()], 7), 4),
        Test(([1] * 100, 50), 51),
    ]

    for tc in cases:
        assert (subarray_sums_1(*tc.inp) == tc.exp)
