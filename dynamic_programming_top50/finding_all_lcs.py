"""
Longest Common Subsequence | Finding all LCS
https://www.techiedelight.com/longest-common-subsequence-finding-lcs/

Given two sequences, print all the possible longest common subsequences present
in them.

For example,

Input:  X = XMJYAUZ, Y = MZJAWXU
Output: MJAU

Input:  X = ABCBDAB, Y = BDCABA
Output: BCAB, BCBA, BDAB
"""
from util import timeit, draw_memo


@timeit
def findall_lcs(a: str, b: str) -> int:
    memo = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            elif memo[i - 1][j] >= memo[i][j - 1]:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = memo[i][j - 1]

    draw_memo(' ' + a, ' ' + b, memo)

    out = set()
    traverse_lcs(a, b, len(a), len(b), memo, [], out)
    return out


def traverse_lcs(a, b, i, j, memo, res, out):
    if memo[i][j] == 0:
        out.add(''.join(reversed(res)))
        return

    if a[i - 1] == b[j - 1]:
        res.append(a[i - 1])
        traverse_lcs(a, b, i - 1, j - 1, memo, res, out)
        res.pop()
        return

    if memo[i - 1][j] >= memo[i][j - 1]:
        traverse_lcs(a, b, i - 1, j, memo, res, out)
    if memo[i - 1][j] <= memo[i][j - 1]:
        traverse_lcs(a, b, i, j - 1, memo, res, out)


if __name__ == '__main__':
    findall_lcs('XMJYAUZ', 'MZJAWXU')
    findall_lcs('ABCBDAB', 'BDCABA')
    findall_lcs('HIEROGLYPHOLOGY', 'MICHAELANGELO')

    """ terminal
    run findall_lcs('XMJYAUZ', 'MZJAWXU')
            M   Z   J   A   W   X   U
        0   0   0   0   0   0   0   0
    X   0   0   0   0   0   0   1   1
    M   0   1   1   1   1   1   1   1
    J   0   1   1   2   2   2   2   2
    Y   0   1   1   2   2   2   2   2
    A   0   1   1   2   3   3   3   3
    U   0   1   1   2   3   3   3   4
    Z   0   1   2   2   3   3   3   4
    got {'MJAU'} in 0.0001106250 secs.

    run findall_lcs('ABCBDAB', 'BDCABA')
            B   D   C   A   B   A
        0   0   0   0   0   0   0
    A   0   0   0   0   1   1   1
    B   0   1   1   1   1   2   2
    C   0   1   1   2   2   2   2
    B   0   1   1   2   2   3   3
    D   0   1   2   2   2   3   3
    A   0   1   2   2   3   3   4
    B   0   1   2   2   3   4   4
    got {'BCBA', 'BDAB', 'BCAB'} in 0.0000781670 secs.

    run findall_lcs('HIEROGLYPHOLOGY', 'MICHAELANGELO')
            M   I   C   H   A   E   L   A   N   G   E   L   O
        0   0   0   0   0   0   0   0   0   0   0   0   0   0
    H   0   0   0   0   1   1   1   1   1   1   1   1   1   1
    I   0   0   1   1   1   1   1   1   1   1   1   1   1   1
    E   0   0   1   1   1   1   2   2   2   2   2   2   2   2
    R   0   0   1   1   1   1   2   2   2   2   2   2   2   2
    O   0   0   1   1   1   1   2   2   2   2   2   2   2   3
    G   0   0   1   1   1   1   2   2   2   2   3   3   3   3
    L   0   0   1   1   1   1   2   3   3   3   3   3   4   4
    Y   0   0   1   1   1   1   2   3   3   3   3   3   4   4
    P   0   0   1   1   1   1   2   3   3   3   3   3   4   4
    H   0   0   1   1   2   2   2   3   3   3   3   3   4   4
    O   0   0   1   1   2   2   2   3   3   3   3   3   4   5
    L   0   0   1   1   2   2   2   3   3   3   3   3   4   5
    O   0   0   1   1   2   2   2   3   3   3   3   3   4   5
    G   0   0   1   1   2   2   2   3   3   3   4   4   4   5
    Y   0   0   1   1   2   2   2   3   3   3   4   4   4   5
    got {'HELLO', 'IELLO', 'IEGLO', 'HEGLO'} in 0.0008864580 secs.
    """
