from util import timeit
from sys import maxsize


@timeit
def apple_division(inp: list[int]) -> None:
    """
    [Easy] https://cses.fi/problemset/task/1623
    [Solution] https://cses.fi/problemset/result/4799511/

    There are n apples with known weights. Your task is to divide the apples 
    into two groups so that the difference between the weights of the groups 
    is minimal.

    The first input line has an integer n: the number of apples.
    The next line has n integers p1,p2,…,pn: the weight of each apple.

    Print one integer: the minimum difference between the weights of the groups.

    Constraints:
    1 ≤ n ≤ 20
    1 ≤ pi ≤ 10^9

    Input:
    5
    3 2 7 4 1

    Output:
    1

    Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 
    has weights 1 and 7 (total weight 8).
    """
    # use bit manipulation techniques to find all subsequences of input array,
    # represent the array of input n as a sequence of bits with value 2^n - 1.
    # if input = [1, 2, 3], n = 3, 2^n - 1 = 7
    # then a subsequence with all array elements will be represented as 111.
    # subsequences with only one element will be represent by the following bits
    # 001 - element 3 from input
    # 010 - element 2 from input...

    # to solve the problem, iterate from [1, 2^n)
    # for every element's index,
    # check if that index should be included in our current subsequence sum.
    total, best = sum(inp), maxsize
    for seq in range(1, 1 << len(inp)):
        curr = 0
        for i, val in enumerate(inp):
            if seq & (1 << i):
                curr += val

        best = min(abs(total - curr - curr), best)

    return best


if __name__ == '__main__':
    apple_division([3, 2, 7, 4, 1])
    apple_division([603, 324, 573, 493, 659, 521, 654, 70, 718, 257])


""" terminal
run apple_division([3, 2, 7, 4, 1])
got 1 in 0.0001142350 secs.

run apple_division([603, 324, 573, 493, 659, 521, 654, 70, 718, 257])
got 2 in 0.0078428360 secs. 
"""
