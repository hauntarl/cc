from util import timeit


@timeit
def permutations(n: str) -> None:
    """
    [Easy] https://cses.fi/problemset/task/1070
    [Solution] https://cses.fi/paste/b5fbcb769d9b7cbc21a5ff/

    A permutation of integers 1,2,…,n is called beautiful if there are no 
    adjacent elements whose difference is 1.

    Given n, construct a beautiful permutation if such a permutation exists. 
    The only input line contains an integer n.

    Print a beautiful permutation of integers 1,2,…,n. If there are several 
    solutions, you may print any of them. If there are no solutions, print 
    "NO SOLUTION".

    Constraints: 1 ≤ n ≤ 10^6

    Example 1
    Input: 5
    Output: 4 2 5 3 1

    Example 2
    Input: 3
    Output: NO SOLUTION
    """
    n = int(n) + 1
    r, p = range, print
    p(*r(2, n, 2), *r(1, n, 2)) if n > 4 or n < 3 else p('NO SOLUTION')


if __name__ == '__main__':
    permutations('1')
    permutations('3')
    permutations('4')
    permutations('5')
    permutations('6')
''' terminal
run permutations('1')
1
got None in 0.0002910000 secs.

run permutations('3')
NO SOLUTION
got None in 0.0001847000 secs.

run permutations('4')
2 4 1 3
got None in 0.0002779000 secs.

run permutations('5')
2 4 1 3 5
got None in 0.0002279000 secs.

run permutations('6')
2 4 6 1 3 5
got None in 0.0002306000 secs.
'''
