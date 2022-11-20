"""
[Easy] https://cses.fi/problemset/task/1090
[Solution] https://cses.fi/paste/62b301efa100eeb94c5064/

There are n children who want to go to a Ferris wheel, and your task is to find
a gondola for each child.

Each gondola may have one or two children in it, and in addition, the total
weight in a gondola may not exceed x. You know the weight of every child.

What is the minimum number of gondolas needed for the children?

The first input line contains two integers n and x: the number of children and
the maximum allowed weight.

The next line contains n integers p1,p2,…,pn: the weight of each child.

Print one integer: the minimum number of gondolas.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ x ≤ 10^9
1 ≤ pi ≤ x

Input:
4 10
7 2 3 9

Output:
3
"""
from util import timeit


@timeit
def ferris_wheel(weights: list[int], limit: int) -> int:
    weights.sort()
    gondolas, i, j = 0, 0, len(weights) - 1
    while i < j:
        if weights[i] + weights[j] <= limit:
            i += 1

        j -= 1
        gondolas += 1

    return gondolas + (1 if i == j else 0)


if __name__ == '__main__':
    ferris_wheel([7, 2, 3, 9], 10)
