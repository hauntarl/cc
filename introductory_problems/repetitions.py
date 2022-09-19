from util import timeit


@timeit
def repetitions(seq: str) -> int:
    """
    [Easy] https://cses.fi/problemset/task/1069/
    [Solution] https://cses.fi/paste/659d805082c50ec1219667/

    You are given a DNA sequence: a string consisting of characters A, C, G, 
    and T. Your task is to find the longest repetition in the sequence. This is 
    a maximum-length substring containing only one type of character.

    The only input line contains a string of n characters.
    Print one integer, the length of the longest repetition.

    Constraints: 1 ≤ n ≤ 10^6

    Example
    Input: ATTCGGGA
    Output: 3
    """
    res, cur = 0, 0
    fir = ''
    for ch in seq:
        if ch == fir:
            cur += 1
        else:
            res = max(res, cur)
            fir = ch
            cur = 1

    return max(res, cur)


if __name__ == '__main__':
    repetitions('ATTCGGGA')
    repetitions('ACCGGGTTTT')
    repetitions('CTCAGGTCCG')
