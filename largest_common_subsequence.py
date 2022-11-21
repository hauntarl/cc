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


if __name__ == '__main__':
    @timeit
    def test(a: str, b: str) -> int: return lcs(a, b, 0, 0, dict())

    test('BDCABA', 'ABCBDAB')
    test('HIEROGLYPHOLOGY', 'MICHAELANGELO')  # HELLO - count=5
