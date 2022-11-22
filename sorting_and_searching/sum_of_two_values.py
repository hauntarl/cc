"""
[Easy] https://cses.fi/problemset/task/1640
[Solution] https://cses.fi/paste/3ccf621fdb0f646c4c6bbe/

You are given an array of n integers, and your task is to find two values (at 
distinct positions) whose sum is x.

The first input line has two integers n and x: the array size and the target 
sum.

The second line has n integers a1,a2,…,an: the array values.

Print two integers: the positions of the values. If there are several solutions,
you may print any of them. If there are no solutions, print IMPOSSIBLE.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ x, ai ≤ 10^9

Input:
4 8
2 7 5 1

Output:
2 4
"""
from util import timeit


@timeit
def sum_of_two_values(nums: list[int], x: int) -> str:
    keep = {}
    for i in range(len(nums)):
        v = nums[i]
        if x - v in keep:
            return f'{keep[x - v] + 1} {i + 1}'

        keep[v] = i

    return 'IMPOSSIBLE'


if __name__ == '__main__':
    assert (sum_of_two_values([2, 7, 5, 1], 8) == '2 4')
    assert (sum_of_two_values([1], 2) == 'IMPOSSIBLE')
    assert (sum_of_two_values([1, 2, 3], 2) == 'IMPOSSIBLE')
    assert (sum_of_two_values([2, 1, 3], 3) == '1 2')
    assert (sum_of_two_values([1, 3, 2], 4) == '1 2')
    assert (sum_of_two_values([1, 2, 3], 5) == '2 3')
    assert (sum_of_two_values([1, 3, 2], 6) == 'IMPOSSIBLE')
    assert (sum_of_two_values([4, 5, 3], 8) == '2 3')
