"""
[Easy] https://cses.fi/problemset/task/1084
[Solution] https://cses.fi/paste/681df3d8abee593b4c3f2c/

There are n applicants and m free apartments. Your task is to distribute the
apartments so that as many applicants as possible will get an apartment.

Each applicant has a desired apartment size, and they will accept any apartment
whose size is close enough to the desired size.

The first input line has three integers n, m, and k: the number of applicants, 
the number of apartments, and the maximum allowed difference.

The next line contains n integers a1,a2,…,an: the desired apartment size of 
each applicant. If the desired size of an applicant is x, he or she will accept
any apartment whose size is between x−k and x+k.

The last line contains m integers b1,b2,…,bm: the size of each apartment.

Print one integer: the number of applicants who will get an apartment.

Constraints:
1 ≤ n, m ≤ 2⋅10^5
0 ≤ k ≤ 10^9
1 ≤ ai, bi ≤ 10^9

Input:
4 3 5
60 45 80 60
30 60 75

Output:
2
"""
from util import timeit
import heapq


@timeit
def apartments(threshold: int, desired: list[int], actual: list[int]) -> int:
    # heapify both the inputs
    heapq.heapify(desired)
    heapq.heapify(actual)

    count = 0
    while desired and actual:
        exp, got = desired[0], actual[0]
        if abs(exp - got) <= threshold:  # if min elements withing threshold
            heapq.heappop(desired)
            heapq.heappop(actual)
            count += 1
        elif exp > got:  # if min of desired > min of actual
            heapq.heappop(actual)
        else:  # if min of actual > min of desired
            heapq.heappop(desired)
    return count


if __name__ == '__main__':
    apartments(
        5,
        [60, 45, 80, 60],
        [30, 60, 75]
    )
    apartments(
        10,
        [90, 41, 20, 39, 49, 21, 35, 31, 74, 86],
        [14, 24, 24, 7, 82, 85, 82, 4, 60, 95]
    )
