from util import timeit


@timeit
def trailing_zeros(n: int) -> int:
    """
    [Easy] https://cses.fi/problemset/task/1618
    [Help] https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
    [Solution] https://cses.fi/paste/e30a1f7b61c0770e239417/

    Your task is to calculate the number of trailing zeros in the factorial n!.
    For example, 20!=2432902008176640000 and it has 4 trailing zeros.

    The only input line has an integer n.
    Print the number of trailing zeros in n!.

    Constraints: 1 ≤ n ≤ 10^9

    Example
    Input: 20
    Output: 4
    """
    c, d = 0, 5
    while n >= d:
        c += n // d
        d *= 5
    return c


if __name__ == '__main__':
    trailing_zeros(20)
    trailing_zeros(11)
    trailing_zeros(5)
    trailing_zeros(395)
    trailing_zeros(374960399)
    trailing_zeros(100000000)

''' terminal
run trailing_zeros(20)
got 4 in 0.0000219000 secs.       

run trailing_zeros(11)
got 2 in 0.0000067000 secs.       

run trailing_zeros(5)
got 1 in 0.0000068000 secs.       

run trailing_zeros(395)
got 97 in 0.0000071000 secs.      

run trailing_zeros(374960399)     
got 93740092 in 0.0000095000 secs.

run trailing_zeros(100000000)
got 24999999 in 0.0000100000 secs.
'''
