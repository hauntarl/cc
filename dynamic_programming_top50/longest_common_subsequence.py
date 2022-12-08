"""
Longest Common Subsequence Problem
https://www.techiedelight.com/longest-common-subsequence/

The Longest Common Subsequence (LCS) problem is finding the longest subsequence
present in given two sequences in the same order, i.e., find the longest
sequence which can be obtained from the first original sequence by deleting
some items and from the second original sequence by deleting other items.

The problem differs from the problem of finding the longest common substring.
Unlike substrings, subsequences are not required to occupy consecutive
positions within the original string.

For example, consider the two following sequences, X and Y:

X: ABCBDAB
Y: BDCABA
 
The length of the LCS is 4
LCS are BDAB, BCAB, and BCBA
"""
from util import timeit


def lcs(a: str, b: str, i: int, j: int, memo: dict) -> int:
    """
    Returns the length of the largest common subsequence from given strings.
    """
    if (i, j) in memo:
        return memo[(i, j)]
    if i >= len(a) or j >= len(b):
        return 0

    size = 0
    if a[i] == b[j]:
        size = 1 + lcs(a, b, i + 1, j + 1, memo)
    else:
        size = max(lcs(a, b, i + 1, j, memo), lcs(a, b, i, j + 1, memo))

    memo[(i, j)] = size
    return size


@timeit
def lcs_bottomup(a: str, b: str) -> int:
    memo = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            elif memo[i - 1][j] >= memo[i][j - 1]:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = memo[i][j - 1]

    return memo[-1][-1]


if __name__ == '__main__':
    @timeit
    def lcs_topdown(a: str, b: str) -> int: return lcs(a, b, 0, 0, dict())

    lcs_topdown('BDCABA', 'ABCBDAB')
    lcs_topdown('HIEROGLYPHOLOGY', 'MICHAELANGELO')  # HELLO - count=5

    lcs_bottomup('BDCABA', 'ABCBDAB')
    lcs_bottomup('HIEROGLYPHOLOGY', 'MICHAELANGELO')  # HELLO - count=5
