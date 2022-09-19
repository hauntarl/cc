from util import timeit


def number_spiral(*tests) -> list:
    """
    [Easy] https://cses.fi/problemset/task/1071
    [Solution] https://cses.fi/paste/4877d985323f074a21baae/

    A number spiral is an infinite grid whose upper-left square has number 1. 
    Here are the first five layers of the spiral:
    1       2       9       10      25
    4       3       8       11      24
    5       6       7       12      23
    16      15      14      13      22
    17      18      19      20      21

    Your task is to find out the number in row y and column x. 

    The first input line contains an integer t: the number of tests. After 
    this, there are t lines, each containing integers y and x.
    For each test, print the number in row y and column x.

    Constraints:
    . 1 ≤ t ≤ 10^5
    . 1 ≤ y, x ≤ 10^9
    """
    r = []
    for t in tests:
        y, x = tuple(map(int, t.split(' ')))
        # find the max axis value from given test:
        m = max(y, x)
        # calc. the value across the diagonal i.e. (m, m):
        # v = m**2 - (m - 1)
        #
        # add offset to value of (m, m) to get value at (y, x):
        # if square(m) is even, the max value for (m, m) lies on y-axis:
        # v += y - x  # move towards the max axis value
        # if square(m) is odd, the max value for (m, m) lies on x-axis
        # v += x - y
        v = m**2 - m + 1 + (y-x if m % 2 == 0 else x-y)
        r.append(v)
    return r


if __name__ == '__main__':
    for r in range(1, 7):
        tests = (f'{r} {c}' for c in range(1, 7))
        print(*number_spiral(*tests), sep='\t')

    print()
    benchmark = timeit(lambda *tests: number_spiral(*tests))
    benchmark('2 3', '1 1', '4 2')
''' terminal
1       2       9       10      25      26
4       3       8       11      24      27
5       6       7       12      23      28
16      15      14      13      22      29
17      18      19      20      21      30
36      35      34      33      32      31

run <lambda>('2 3', '1 1', '4 2')
got [8, 1, 15] in 0.0000378000 secs.
'''
