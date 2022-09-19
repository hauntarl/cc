"""
Given an array of n numbers, calculate the maximum subarray sum, i.e., the 
largest possible sum of a sequence of consecutive values in the array. The 
problem is interesting when there may be negative values in the array.

For example, in the array: [-1, 2, 4, -3, 5, 2, -5, 2]
the following subarray produces the maximum sum 10: [2, 4, -3, 5, 2]

We assume that an empty subarray is allowed, so the maximum subarray sum is 
always at least 0.
"""
from util import timeit


@timeit
def algorithm_1(array: list) -> int:
    """
    Algorithm 1 - Brute Force

    A straightforward way to solve the problem is to go through all possible 
    subarrays, calculate the sum of values in each subarray and maintain the 
    maximum sum.

    The variables [i] and [j] fix the first and last index of the subarray, and 
    the sum of values is calculated to the variable [cur]. The variable [best] 
    contains the maximum sum found during the search.

    The time complexity of the algorithm is O(n^3), because it consists of 
    three nested loops that go through the input.
    """
    best = 0
    size = len(array)
    for i in range(0, size):
        for j in range(i, size):
            curr = 0  # sum of current subarray
            for k in range(i, j):
                curr += array[k]
            best = max(best, curr)

    return best


@timeit
def algorithm_2(array: list) -> int:
    """
    Algorithm 2 - Brute Force Optimized

    It is easy to make Algorithm 1 more efficient by removing one loop from it. 
    This is possible by calculating the sum at the same time when the right end 
    of the subarray moves.

    The time complexity is O(n^2).
    """
    best = 0
    size = len(array)
    for i in range(0, size):
        curr = 0
        for j in range(i, size):
            curr += array[j]
            best = max(best, curr)

    return best


@timeit
def algorithm_3(arr: list) -> int:
    """
    Algorithm 3 - Kadane’s Algorithm

    The idea is to calculate, for each array position, the maximum sum of a 
    subarray that ends at that position. After this, the answer for the problem 
    is the maximum of those sums.

    Consider the subproblem of finding the maximum-sum subarray that ends at
    position k. There are two possibilities:
    . The subarray only contains the element at position k
    . The subarray consists of a subarray that ends at position k−1, followed 
      by the element at position k
    In the latter case, since we want to find a subarray with maximum sum, the
    subarray that ends at position k −1 should also have the maximum sum. Thus,
    we can solve the problem efficiently by calculating the maximum subarray 
    sum for each ending position from left to right.

    The algorithm only contains one loop that goes through the input, so the 
    time complexity is O(n). This is also the best possible time complexity, 
    because any algorithm for the problem has to examine all array elements at 
    least once.
    """
    best, curr = 0, 0
    for elem in arr:
        curr = max(elem, curr + elem)
        best = max(best, curr)

    return best


arr = [-1, 2, 4, -3, 5, 2, -5, 2]
algorithm_1(arr)
algorithm_2(arr)
algorithm_3(arr)
''' terminal
run algorithm_1([-1, 2, 4, -3, 5, 2, -5, 2])
got '10' in 0.0001549000 secs.

run algorithm_2([-1, 2, 4, -3, 5, 2, -5, 2])
got '10' in 0.0001001000 secs.

run algorithm_3([-1, 2, 4, -3, 5, 2, -5, 2])
got '10' in 0.0000287000 secs.
'''
