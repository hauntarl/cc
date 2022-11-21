"""
[Medium] https://cses.fi/problemset/task/1091

There are n concert tickets available, each with a certain price. Then, m
customers arrive, one after another.

Each customer announces the maximum price they are willing to pay for a ticket,
and after this, they will get a ticket with the nearest possible price such
that it does not exceed the maximum price.

The first input line contains integers n and m: the number of tickets and the
number of customers.

The next line contains n integers h1,h2,…,hn: the price of each ticket.

The last line contains m integers t1,t2,…,tm: the maximum price for each
customer in the order they arrive.

Print, for each customer, the price that they will pay for their ticket. After
this, the ticket cannot be purchased again.

If a customer cannot get any ticket, print -1.

Constraints:
1 ≤ n, m ≤ 2⋅10^5
1 ≤ hi, ti ≤ 10^9

Input:
5 3
5 3 7 8 5
4 8 3

Output:
3
8
-1
"""
# pip install sortedcontainers - to get the package
from sortedcontainers import SortedDict
from util import timeit


@timeit
def concert_tickets(tickets: list[int], prices: list[int]) -> list[int]:
    """
    In order to solve this problem, we need an ADT with the following:
    . random access - O(1) look up
    . efficient search - O(log n)

    Basically, we need a Data Structure that keeps its items sorted with a 
    constant time look up i.e. TreeMap.
    In Python, we don't have a built-in collection that provides this 
    functionality, hence we need to use the SortedDict from sortedcontainers
    package to fullfill this requirement.

    This will reduce the time complexity to O(m.log n)
    """
    # * create a sorted dictionary that maintains the frequency of each item
    freq = SortedDict()
    for t in tickets:
        freq[t] = (freq[t] + 1) if t in freq else 1

    res = []
    # * iterate over prices and find closest <= ticket for the given price
    for p in prices:
        if p in freq:
            # * if there is an exact match, assign that ticket to the customer
            freq[p] -= 1
            if freq[p] == 0:
                del freq[p]
            res.append(p)
        else:
            # * if exact match not available, find closest minimum ticket
            i = freq.bisect(p) - 1
            if i < 0:
                # * if no ticket is <= given price
                res.append(-1)
                continue

            t, f = freq.peekitem(i)
            if f - 1 == 0:
                del freq[t]
            else:
                freq[t] = f - 1

            res.append(t)

    return res


if __name__ == '__main__':
    assert (
        concert_tickets([5, 3, 7, 8, 5], [4, 8, 3]) == [3, 8, -1]
    )
    assert (
        concert_tickets([1] * 10, [1] * 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    )
    assert (
        concert_tickets([1], [10, 10]) == [1, -1]
    )
    assert (
        concert_tickets([2, 2, 2], [4, 4, 4, 4]) == [2, 2, 2, -1]
    )
    assert (
        concert_tickets(
            [int(v) for v in '9 3 9 6 6 8 6 2 6 3'.split()],
            [int(v) for v in '9 5 4 6 3 9 3 3 5 2'.split()]
        ) == [9, 3, 3, 6, 2, 9, -1, -1, -1, -1]
    )
