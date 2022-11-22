"""
[Easy] https://cses.fi/problemset/task/1629
[Solution] https://cses.fi/paste/f0fb6e57063a91d14c6b63/

In a movie festival n movies will be shown. You know the starting and ending 
time of each movie. What is the maximum number of movies you can watch 
entirely?

The first input line has an integer n: the number of movies.

After this, there are n lines that describe the movies. Each line has two 
integers a and b: the starting and ending times of a movie.

Print one integer: the maximum number of movies.

Constraints:
1 ≤ n ≤ 2⋅10^5
1 ≤ a < b ≤ 10^9

Input:
3
3 5
4 9
5 8

Output:
2
"""
from util import timeit


@timeit
def movie_festival(times: list[tuple[int, int]]) -> int:
    """
    Sort the movie timings based on end time for each movie.
    Iterate over movie timings,
    . compare the start of current movie with end of last watched movie
    . if the start of current movie >= the end of last watched movie
        . increment movies watched counter
        . update index for last watched movie to current movie
    """
    times.sort(key=lambda t: t[1])
    i, movies = 0, 1
    for j in range(1, len(times)):
        s, _ = times[j]
        if times[i][1] <= s:
            i = j
            movies += 1

    return movies


if __name__ == '__main__':
    assert (movie_festival([(1, 2), (3, 4)]) == 2)
    assert (movie_festival([(3, 5), (4, 9), (5, 8)]) == 2)
    assert (movie_festival([(1, 1000), (2, 3), (5, 6)]) == 2)
    assert (movie_festival([(1, 1000)] * 10) == 1)
    assert (movie_festival(
        [(6, 7), (4, 5), (8, 9), (2, 3), (10, 11), (1, 2),
         (9, 10), (3, 4), (5, 6), (7, 8)]) == 10
    )
    assert (movie_festival(
        [(404, 882), (690, 974), (201, 255), (800, 933), (525, 819),
         (457, 601), (461, 978), (832, 932), (699, 804), (795, 860)]) == 4
    )
