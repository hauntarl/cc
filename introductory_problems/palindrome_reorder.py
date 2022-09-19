from util import timeit
from collections import Counter


@timeit
def palindrome_reorder(inp: str) -> None:
    """
    [Easy] https://cses.fi/problemset/task/1755/
    [Solution] https://cses.fi/paste/3f6b2d02a344693647026e/

    Given a string, your task is to reorder its letters in such a way that it 
    becomes a palindrome (i.e., it reads the same forwards and backwards).

    The only input line has a string of length n consisting of characters A–Z.

    Print a palindrome consisting of the characters of the original string. You 
    may print any valid solution. If there are no solutions, print 
    "NO SOLUTION".

    Constraints:
    1 ≤ n ≤ 10^6

    Input:
    AAAACACBA

    Output:
    AACABACAA
    """
    if inp == '':
        return "NO SOLUTION"

    freq = Counter(inp)
    even, odd, size = [], None, 0
    for ch, count in freq.items():
        size += count
        if not count & 1:
            even.append((ch, count))
        elif not odd:
            odd = (ch, count)
        else:
            return "NO SOLUTION"

    res, beg, end = [None] * size, 0, size
    for ch, count in even:
        lim = count // 2
        sub = [ch] * lim
        res[beg: beg + lim] = sub
        res[end - lim: end] = sub
        beg += lim
        end -= lim

    if odd:
        res[beg: end] = [odd[0]] * odd[1]

    return ''.join(res)


if __name__ == '__main__':
    palindrome_reorder('AAAACACBA')
    palindrome_reorder('AAAACACBAB')
    palindrome_reorder('AAAACACBAC')
    palindrome_reorder('AAAACACBACB')
    palindrome_reorder('AAAACACBABBC')

''' terminal
run palindrome_reorder('AAAACACBA')
got AAACBCAAA in 0.0002121350 secs.

run palindrome_reorder('AAAACACBAB')
got AAACBBCAAA in 0.0000409430 secs.

run palindrome_reorder('AAAACACBAC')
got NO SOLUTION in 0.0000272410 secs.

run palindrome_reorder('AAAACACBACB')
got AAABCCCBAAA in 0.0000340930 secs.

run palindrome_reorder('AAAACACBABBC')
got NO SOLUTION in 0.0000258780 secs.
'''
