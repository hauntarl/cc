"""
[Medium] https://cses.fi/problemset/task/1073
[Solution] https://cses.fi/paste/52847370ebc365494ca1ee/

You are given n cubes in a certain order, and your task is to build towers
using them. Whenever two cubes are one on top of the other, the upper cube must
be smaller than the lower cube.

You must process the cubes in the given order. You can always either place the
cube on top of an existing tower, or begin a new tower. What is the minimum
possible number of towers?

The first input line contains an integer n: the number of cubes.

The next line contains n integers k1,k2,…,kn: the sizes of the cubes.

Print one integer: the minimum number of towers.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ ki ≤ 10^9

Input:
5
3 8 2 1 5

Output:
2
"""
from util import timeit


def search(items: list[int], key: int) -> int:
    """
    Alternate binary search,
    returns the position where the key should ideally be.
    """
    i, k = len(items) // 2, 0
    while i > 0:
        while i + k < len(items) and items[i + k] <= key:
            k += i
        i >>= 1

    if items[k] <= key:
        k += 1
    return k


@timeit
def towers(cubes: list[int]) -> int:
    res = [cubes[0]]
    for i in range(1, len(cubes)):
        c = cubes[i]
        j = search(res, c)
        if j == len(res):
            res.append(c)
        else:
            res[j] = c
    return len(res)


if __name__ == '__main__':
    from collections import namedtuple

    Test = namedtuple('Test', ['inp', 'exp'])
    cases = [
        Test([int(v) for v in '3 8 2 1 5'.split()], 2),
        Test([int(v) for v in '1 1 1 1 1 1 1 1 1 1'.split()], 10),
        Test([int(v) for v in '10 4 5 9 4 10 2 7 4 6'.split()], 4),
        Test([int(v) for v in '1 2 3 4 5 8 7 1 9 1'.split()], 7),
        Test([int(v) for v in '1 2 3 4 5 8 7 1 9 1'.split()], 7),
        Test([int(v) for v in '10 9 8 7 6 10 4 3 2 1'.split()], 2),
        Test([int(v) for v in '5 5 3 4'.split()], 2),
        Test([int(v) for v in '2 9 2 4'.split()], 3),
    ]

    for tc in cases:
        assert (towers(tc.inp) == tc.exp)
