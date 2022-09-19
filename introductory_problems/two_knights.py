from util import timeit


class Board:
    def __init__(self, size) -> None:
        self.size = size


@timeit
def two_knights(n: int) -> tuple:
    """
    [Medium] https://cses.fi/problemset/task/1072
    [Solution] https://cses.fi/paste/f79701a140ee5c27220d5b/

    Your task is to count for k=1,2,…,n the number of ways two knights can be 
    placed on a k×k chessboard so that they do not attack each other.

    The only input line contains an integer n.
    Print n integers: the results.
    Constraints: 1 ≤ n ≤ 10000
    """
    # 1 calc. all unique combinations for two knights on a kxk chessboard:
    # - total no. of ways to put 1st knight = k^2
    # - total no. of ways to put 2nd knight = k^2 - 1
    # - remove combinations when the knights switch positions = divide / 2
    # - unq_combinations = (k^2(k^2-1))/2 i.e. k^2C2 combinations
    #
    # 2 calc. all the combinations where the two knights threaten each other:
    # - in a rectangle of 2x3 we have 2 positions where they threaten each other
    #   - calc. total number of 2x3 rectangles that fit in given kxk chessboard
    #   - i.e (k-1)(k-2)
    #   - number of positions where they threaten each other are: 2(k-1)(k-2)
    # - similarly in a 3x2 we have 2(k-1)(k-2) positions
    # - total number of ways they can threaten each other are: 4(k-1)(k-2)
    #
    # 3 subtract positions that threaten each other from unq_combinations:
    # - k^2C2 - 4(k-1)(k-2)
    return tuple((k*k*(k*k-1)//2 - 4*(k-1)*(k-2)) for k in range(1, n+1))


if __name__ == '__main__':
    two_knights(8)
''' terminal
run two_knights(8)
got (0, 6, 28, 96, 252, 550, 1056, 1848) in 0.0000467000 secs.
'''
