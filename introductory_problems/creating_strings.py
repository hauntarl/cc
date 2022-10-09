from util import timeit


@timeit
def creating_strings(inp: list[str], beg: int, func) -> None:
    """
    [Easy] https://cses.fi/problemset/task/1622
    [Solution] https://cses.fi/problemset/result/4779301/

    Given a string, your task is to generate all different strings that can be 
    created using its characters.

    The only input line has a string of length n. Each character is between a–z.

    First print an integer k: the number of strings. Then print k lines: the 
    strings in alphabetical order.

    Constraints:
    1 ≤ n ≤ 8

    Input:
    aabac

    Output:
    20
    aaabc
    aaacb
    aabac
    aabca
    aacab
    aacba
    abaac
    abaca
    abcaa
    acaab
    acaba
    acbaa
    baaac
    baaca
    bacaa
    bcaaa
    caaab
    caaba
    cabaa
    cbaaa
    """
    if len(inp) - beg < 2:
        func(''.join(inp))
        return

    creating_strings(inp, beg + 1, func)
    for cur in range(beg + 1, len(inp)):
        inp[beg], inp[cur] = inp[cur], inp[beg]
        creating_strings(inp, beg + 1, func)
        inp[beg], inp[cur] = inp[cur], inp[beg]


if __name__ == '__main__':
    perms = set()
    creating_strings(sorted('aabac'), 0, perms.add)
    print(len(perms), '\n'.join(sorted(perms)), sep='\n')
