"""
[Medium] https://cses.fi/problemset/task/1141
[Solution] https://cses.fi/paste/3152554e0dfae6fc4ca174/

You are given a playlist of a radio station since its establishment. The
playlist has a total of n songs.

What is the longest sequence of successive songs where each song is unique?

The first input line contains an integer n: the number of songs.

The next line has n integers k1,k2,…,kn: the id number of each song.

Print the length of the longest sequence of unique songs.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ ki ≤ 10^9

Input:
8
1 2 1 3 2 7 4 2

Output:
5
"""
from collections import OrderedDict
from util import timeit


def playlist_dc(songs: list[int]) -> int:
    """
    Divide and Conquer solution to the given problem.
    . divide - divide the input into two havles
        . recursively solve the left half
        . recursively solve the right half
    . combine - find the count of unique elements from the mid across the input
    . return maximum of left, right and combine results

    Note: Causes Time Limit Exceeded error :(
    """
    if len(songs) < 2:
        return len(songs)

    mid, unq = len(songs) // 2, set()
    unq.add(songs[mid])
    for i in range(mid - 1, -1, -1):
        if songs[i] in unq:
            break
        unq.add(songs[i])

    for i in range(mid + 1, len(songs)):
        if songs[i] in unq:
            break
        unq.add(songs[i])

    if len(unq) > mid:
        return len(unq)
    return max(playlist_dc(songs[:mid]), playlist_dc(songs[mid:]), len(unq))


@timeit
def playlist(songs: list[int]) -> int:
    """
    Efficient algorithm to solve the given problem.
    Use an ordered dictionary to maintain the insertion order of elements.
    . iterate over all the songs
        . if this song hasn't been played before, insert into dictionary
        . if song has been played
            . remove all elements from the front till the current song
            . insert the current song into the dictionary
    """
    unq, res = OrderedDict(), 0
    for s in songs:
        if s not in unq:
            unq[s] = None
        else:
            res = max(res, len(unq))
            while unq and unq.popitem(last=False)[0] != s:
                pass
            unq[s] = None

    return max(res, len(unq))


if __name__ == '__main__':
    from collections import namedtuple

    Test = namedtuple('Test', ['inp', 'exp'])
    cases = [
        Test([int(v) for v in '1 2 1 3 2 7 4 2'.split()], 5),
        Test([int(v) for v in '1 1 1 1 1 1 1 1 1 1'.split()], 1),
        Test([int(v) for v in '2 2 1 1 2 1 2 1 2 1'.split()], 2),
        Test([int(v) for v in '3 3 3 3 5 1 5 1 1 4'.split()], 3),
        Test([int(v) for v in '45 9 37 81 69 99 49 71 90 30'.split()], 10),
        Test([int(v) for v in '1 1 3 4 5'.split()], 4),
        Test([int(v) for v in '2 3 4 5 2 10 9 8 6 1'.split()], 9),
    ]

    @timeit
    def test(songs: list[int]) -> int: return playlist_dc(songs)

    for tc in cases:
        assert (test(tc.inp) == tc.exp)
    for tc in cases:
        assert (playlist(tc.inp) == tc.exp)
