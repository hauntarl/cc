"""
[Medium] https://cses.fi/problemset/task/2183/
[Solution] https://cses.fi/paste/9d3564970ac5cc744ca09e/

You have n coins with positive integer values. What is the smallest sum you
cannot create using a subset of the coins?

The first input line has an integer n: the number of coins.

The second line has n integers x1,x2,…,xn: the value of each coin.

Print one integer: the smallest coin sum.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ xi ≤ 10^9

Input:
5
2 9 1 2 7

Output:
6
"""
from util import timeit


@timeit
def missing_coin_sum(coins: list[int]) -> int:
    coins.sort()
    res = 1
    for c in coins:
        if res < c:
            break
        res += c
    return res


if __name__ == '__main__':
    from collections import namedtuple

    Test = namedtuple('Test', ['inp', 'exp'])
    cases = [
        Test([int(v) for v in '2 9 1 2 7'.split()], 6),
        Test([int(v) for v in '2 1 4 3'.split()], 11),
        Test([int(v) for v in '2 2 2 2'.split()], 1),
        Test([int(v) for v in '1 9 9 1 2 2'.split()], 7),
        Test([int(v) for v in '1 1 1 1 1 1 1 1 2 7'.split()], 18),
    ]

    for tc in cases:
        assert (missing_coin_sum(tc.inp) == tc.exp)
