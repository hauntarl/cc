"""
Longest Palindromic Subsequence using Dynamic Programming
https://www.techiedelight.com/longest-palindromic-subsequence-using-dynamic-programming/

The Longest Palindromic Subsequence (LPS) problem is finding the longest
subsequences of a string that is also a palindrome.

The problem differs from the problem of finding the longest palindromic
substring. Unlike substrings, subsequences are not required to occupy
consecutive positions within the original string.
 
For example, consider the sequence ABBDCACB.

The length of the longest palindromic subsequence is 5
The longest palindromic subsequence is BCACB
"""
from util import timeit, draw_memo


def lps(a: str, i: int, j: int, memo: dict) -> int:
    if (i, j) in memo:
        return memo[(i, j)]
    if i == j:
        return 1
    if i > j:
        return 0

    if a[i] == a[j]:
        res = lps(a, i + 1, j - 1, memo) + 2
    else:
        res = max(lps(a, i + 1, j, memo), lps(a, i, j - 1, memo))

    memo[(i, j)] = res
    return res


@timeit
def lps_bottomup(a: str) -> int:
    n, b = len(a) + 1, a[::-1]
    memo = [[0] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if a[i - 1] == b[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    draw_memo(' ' + a, ' ' + b, memo)
    out = set()
    traverse_lps(a, b, n - 1, n - 1, [], out, memo)
    return memo[-1][-1], out


def traverse_lps(a, b, i, j, res, out, memo):
    if memo[i][j] == 0:
        out.add(''.join(res))
        return

    if a[i - 1] == b[j - 1]:
        res.append(a[i - 1])
        traverse_lps(a, b, i - 1, j - 1, res, out, memo)
        res.pop()
        return

    if memo[i - 1][j] >= memo[i][j - 1]:
        traverse_lps(a, b, i - 1, j, res, out, memo)
    if memo[i - 1][j] <= memo[i][j - 1]:
        traverse_lps(a, b, i, j - 1, res, out, memo)


if __name__ == '__main__':
    @timeit
    def lps_topdown(a): return lps(a, 0, len(a) - 1, {})

    lps_topdown('ABBDCACB')
    lps_topdown('ABBDCCB')
    lps_topdown('ABBDCAB')
    lps_topdown('CACBAB')

    lps_bottomup('ABBDCACB')
    lps_bottomup('ABBDCCB')
    lps_bottomup('ABBDCAB')
    lps_bottomup('CACBAB')

    """ terminal
    run lps_topdown('ABBDCACB')
    got 5 in 0.0000110000 secs.

    run lps_topdown('ABBDCCB')
    got 4 in 0.0000058330 secs.

    run lps_topdown('ABBDCAB')
    got 4 in 0.0000036670 secs.

    run lps_topdown('CACBAB')
    got 3 in 0.0000071670 secs.

    run lps_bottomup('ABBDCACB')
            B   C   A   C   D   B   B   A
        0   0   0   0   0   0   0   0   0
    A   0   0   0   1   1   1   1   1   1
    B   0   1   1   1   1   1   2   2   2
    B   0   1   1   1   1   1   2   3   3
    D   0   1   1   1   1   2   2   3   3
    C   0   1   2   2   2   2   2   3   3
    A   0   1   2   3   3   3   3   3   4
    C   0   1   2   3   4   4   4   4   4
    B   0   1   2   3   4   4   5   5   5
    got (5, {'BCACB'}) in 0.0000640000 secs.

    run lps_bottomup('ABBDCCB')
            B   C   C   D   B   B   A
        0   0   0   0   0   0   0   0
    A   0   0   0   0   0   0   0   1
    B   0   1   1   1   1   1   1   1
    B   0   1   1   1   1   2   2   2
    D   0   1   1   1   2   2   2   2
    C   0   1   2   2   2   2   2   2
    C   0   1   2   3   3   3   3   3
    B   0   1   2   3   3   4   4   4
    got (4, {'BCCB'}) in 0.0000404590 secs.

    run lps_bottomup('ABBDCAB')
            B   A   C   D   B   B   A
        0   0   0   0   0   0   0   0
    A   0   0   1   1   1   1   1   1
    B   0   1   1   1   1   2   2   2
    B   0   1   1   1   1   2   3   3
    D   0   1   1   1   2   2   3   3
    C   0   1   1   2   2   2   3   3
    A   0   1   2   2   2   2   3   4
    B   0   1   2   2   2   3   3   4
    got (4, {'ABBA'}) in 0.0000375420 secs.

    run lps_bottomup('CACBAB')
            B   A   B   C   A   C
        0   0   0   0   0   0   0
    C   0   0   0   0   1   1   1
    A   0   0   1   1   1   2   2
    C   0   0   1   1   2   2   3
    B   0   1   1   2   2   2   3
    A   0   1   2   2   2   3   3
    B   0   1   2   3   3   3   3
    got (3, {'CAC', 'ABA', 'ACA', 'BAB'}) in 0.0000630420 secs.
    """
