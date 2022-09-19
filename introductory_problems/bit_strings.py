from util import timeit


@timeit
def bit_strings(n: int) -> int:
    """
    [Easy] https://cses.fi/problemset/task/1617/
    [Solution] https://cses.fi/paste/7b6a02a0d99b6e2022b83f/

    Your task is to calculate the number of bit strings of length n.

    For example, if n=3, the correct answer is 8, because the possible bit 
    strings are 000, 001, 010, 011, 100, 101, 110, and 111.

    The only input line has an integer n.
    Print the result modulo 109+7.

    Constraints: 1 ≤ n ≤ 10^6

    Example
    Input: 3
    Output: 8
    """
    return (2 << n-1) % (10**9+7)


if __name__ == '__main__':
    bit_strings(3)
    bit_strings(7)
    bit_strings(15)
''' terminal
run bit_strings(3)
got 8 in 0.0000288000 secs.    

run bit_strings(7)
got 128 in 0.0000046000 secs.  

run bit_strings(15)
got 32768 in 0.0000051000 secs.
'''
