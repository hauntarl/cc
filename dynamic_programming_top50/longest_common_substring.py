"""
Longest Common Substring Problem
https://www.techiedelight.com/longest-common-substring-problem/

The longest common substring problem is the problem of finding the longest
string (or strings) that is a substring (or are substrings) of two strings.

The problem differs from the problem of finding the Longest Common Subsequence
(LCS). Unlike subsequences, substrings are required to occupy consecutive
positions within the original string.

For example, the longest common substring of strings ABABC, BABCA is the string
BABC having length 4. Other common substrings are ABC, A, AB, B, BA, BC, and C.
"""
from util import timeit, draw_memo


def lcs(a: str, b: str, i: int, j: int, best: int, memo: dict) -> int:
    if (i, j, best) in memo:
        return memo[(i, j, best)]
    if i < 0 or j < 0:
        return best

    if a[i] == b[j]:
        res = max(
            lcs(a, b, i - 1, j - 1, best + 1, memo),
            best
        )
    else:
        res = max(
            lcs(a, b, i - 1, j, 0, memo),
            lcs(a, b, i, j - 1, 0, memo),
            best
        )

    memo[(i, j, best)] = res
    return res


@timeit
def lcs_bottomup(a: str, b: str) -> int:
    n, m = len(a) + 1, len(b) + 1
    memo = [[0] * m for _ in range(n)]
    best = 0
    for i in range(1, n):
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
                best = max(memo[i][j], best)
            else:
                memo[i][j] = 0

    draw_memo(' ' + a, ' ' + b, memo)
    return best


if __name__ == '__main__':
    @timeit
    def lcs_topdown(a, b): return lcs(a, b, len(a) - 1, len(b) - 1, 0, {})

    lcs_topdown('ABABC', 'BABCA')
    lcs_bottomup('ABABC', 'BABCA')

    lcs_topdown('BDCABA', 'ABCBDAB')
    lcs_bottomup('BDCABA', 'ABCBDAB')

    lcs_topdown('ABCHAUNTARL', 'HAUNTARLABC')
    lcs_bottomup('ABCHAUNTARL', 'HAUNTARLABC')

    """ terminal
    run lcs_topdown('ABABC', 'BABCA')
    got 4 in 0.0000248330 secs.

    run lcs_bottomup('ABABC', 'BABCA')
            B   A   B   C   A
        0   0   0   0   0   0
    A   0   0   1   0   0   1
    B   0   1   0   2   0   0
    A   0   0   2   0   0   1
    B   0   1   0   3   0   0
    C   0   0   0   0   4   0
    got 4 in 0.0000587500 secs.

    run lcs_topdown('BDCABA', 'ABCBDAB')
    got 2 in 0.0000219580 secs.

    run lcs_bottomup('BDCABA', 'ABCBDAB')
            A   B   C   B   D   A   B
        0   0   0   0   0   0   0   0
    B   0   0   1   0   1   0   0   1
    D   0   0   0   0   0   2   0   0
    C   0   0   0   1   0   0   0   0
    A   0   1   0   0   0   0   1   0
    B   0   0   2   0   1   0   0   2
    A   0   1   0   0   0   0   1   0
    got 2 in 0.0000577920 secs.

    run lcs_topdown('ABCHAUNTARL', 'HAUNTARLABC')
    got 8 in 0.0000730830 secs.

    run lcs_bottomup('ABCHAUNTARL', 'HAUNTARLABC')
            H   A   U   N   T   A   R   L   A   B   C
        0   0   0   0   0   0   0   0   0   0   0   0
    A   0   0   1   0   0   0   1   0   0   1   0   0
    B   0   0   0   0   0   0   0   0   0   0   2   0
    C   0   0   0   0   0   0   0   0   0   0   0   3
    H   0   1   0   0   0   0   0   0   0   0   0   0
    A   0   0   2   0   0   0   1   0   0   1   0   0
    U   0   0   0   3   0   0   0   0   0   0   0   0
    N   0   0   0   0   4   0   0   0   0   0   0   0
    T   0   0   0   0   0   5   0   0   0   0   0   0
    A   0   0   1   0   0   0   6   0   0   1   0   0
    R   0   0   0   0   0   0   0   7   0   0   0   0
    L   0   0   0   0   0   0   0   0   8   0   0   0
    got 8 in 0.0001132090 secs.
    """
