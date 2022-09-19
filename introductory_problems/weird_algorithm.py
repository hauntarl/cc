from util import timeit


@timeit
def weird_algorithm(n: int) -> None:
    """
    [Easy] https://cses.fi/problemset/task/1068/
    [Solution] https://cses.fi/paste/658ec88d6edc689f217b7f/

    Consider an algorithm that takes as input a positive integer n. If n is 
    even, the algorithm divides it by two, and if n is odd, the algorithm 
    multiplies it by three and adds one. The algorithm repeats this, until n is 
    one. For example, the sequence for n=3 is as follows:
    3 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    Simulate the execution of the algorithm for a given value of n.

    Constraints: 1 ≤ n ≤ 10^6

    Example
    Input : 3
    Output: 3 10 5 16 8 4 2 1
    """
    while n > 1:
        print(n, end=' ')
        n = n // 2 if n % 2 == 0 else n * 3 + 1
    print(n)


if __name__ == '__main__':
    weird_algorithm(3)
    weird_algorithm(7)
    weird_algorithm(15)
''' terminal
run weird_algorithm(3)
3 10 5 16 8 4 2 1
got None in 0.0005022000 secs.

run weird_algorithm(7)
7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
got None in 0.0005121000 secs.

run weird_algorithm(15)
15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1
got None in 0.0007321000 secs.
'''
