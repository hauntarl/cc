"""
[Easy] https://cses.fi/problemset/task/1619

You are given the arrival and leaving times of n customers in a restaurant.
What was the maximum number of customers in the restaurant at any time?

The first input line has an integer n: the number of customers.

After this, there are n lines that describe the customers. Each line has two 
integers a and b: the arrival and leaving times of a customer.

You may assume that all arrival and leaving times are distinct.

Print one integer: the maximum number of customers.

Constraints:
1 ≤ n ≤ 2⋅10^5 
1 ≤ a < b ≤ 10^9

Input:
3
5 8
2 4
3 9

Output:
2
"""
from sortedcontainers import SortedSet
from util import timeit


@timeit
def restaurant_customer(logs: list[tuple[int, int]]) -> int:
    """
    2, 4 -> find customers with departure time <= 2 = 0, count = 1 - 0
    3, 9 -> find customers with departure time <= 3 = 0, count = 2 - 0
    5, 8 -> find customers with departure time <= 5 = 1, count = 3 - 1
    maximum customers at any given point in the restaurant = 2.

    ADT required to solve this efficiently is TreeSet i.e. SortedSet in python
    """
    logs.sort()
    dep, cap = SortedSet(), 0
    for a, d in logs:
        dep.add(d)
        # * find closest departure <= arrival a
        i = dep.index(a) if a in dep else (dep.bisect(a) - 1)
        cap = max(cap, len(dep) - i - 1)
    return cap


if __name__ == '__main__':
    assert (restaurant_customer([(5, 8), (2, 4), (3, 9)]) == 2)
    assert (restaurant_customer([(1, 10), (2, 4), (3, 5), (7, 9)]) == 3)
    assert (restaurant_customer(
        [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12),
         (13, 14), (15, 16), (17, 18), (19, 20)]) == 1
    )
    assert (restaurant_customer(
        [(1, 20), (2, 19), (3, 18), (4, 17), (5, 16), (6, 15),
         (7, 14), (8, 13), (9, 12), (10, 11)]) == 10
    )
    assert (restaurant_customer(
        [(45, 84), (2, 43), (34, 64), (42, 99), (50, 80),
         (12, 21), (72, 82), (39, 86), (33, 89), (47, 97)]) == 7
    )
