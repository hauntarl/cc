from util import timeit


@timeit
def two_sets(num: int) -> tuple:
    """
    [Easy] https://cses.fi/problemset/task/1092
    [Solution] https://cses.fi/paste/c902e83ffcb2ff1c2424f6/

    Your task is to divide the numbers 1,2,…,n into two sets of equal sum.

    The only input line contains an integer n.
    Print "YES", if the division is possible, and "NO" otherwise.
    After this, if the division is possible, print an example of how to create 
    the sets. First, print the number of elements in the first set followed by 
    the elements themselves in a separate line, and then, print the second set 
    in a similar way.

    Constraints: 1 ≤ n ≤ 10^6

    Example 1
    Input: 7
    Output: ((1, 2, 4, 7), (3, 5, 6))

    Example 2
    Input: 6
    Output: None
    """
    net = num * (num + 1) >> 1
    if net & 1:
        return None

    net >>= 1
    one = []
    cur, beg = 0, 1
    if net % num == 0:
        one.append(num)
        cur += num
    else:
        num += 1

    while cur != net:
        one.extend((beg, num - beg))
        cur += num
        beg += 1

    return (tuple(one), tuple(range(beg, num - beg + 1)))


if __name__ == '__main__':
    two_sets(6)
    two_sets(7)
    two_sets(8)
    two_sets(12)
    two_sets(15)
''' terminal
run two_sets(6)
got None in 0.0000124000 secs.

run two_sets(7)
got ((7, 1, 6), (2, 3, 4, 5)) in 0.0000426000 secs.

run two_sets(8)
got ((1, 8, 2, 7), (3, 4, 5, 6)) in 0.0000422000 secs.

run two_sets(12)
got ((1, 12, 2, 11, 3, 10), (4, 5, 6, 7, 8, 9)) in 0.0000495000 secs.

run two_sets(15)
got ((15, 1, 14, 2, 13, 3, 12), (4, 5, 6, 7, 8, 9, 10, 11)) in 0.0000667000 secs.
'''
