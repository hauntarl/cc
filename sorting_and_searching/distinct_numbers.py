"""
[Easy] https://cses.fi/problemset/task/1621/
[Solution] https://cses.fi/paste/2277298fb43b37244c3e2a/

You are given a list of n integers, and your task is to calculate the number of 
distinct values in the list.

The first input line has an integer n: the number of values.
The second line has n integers x1,x2,…,xn.

Print one integers: the number of distinct values.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ xi ≤ 10^9

Input:
5
2 3 2 2 3

Output:
2
"""
from util import timeit


@timeit
def distinct_numbers(numbers: list[int]) -> int:
    return len(set(numbers))


if __name__ == '__main__':
    distinct_numbers([2, 3, 2, 2, 3])
