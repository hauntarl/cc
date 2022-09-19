from util import timeit


@timeit
def increasing_array(_: str, arr: str) -> int:
    """
    [Easy] https://cses.fi/problemset/task/1094/
    [Solution] https://cses.fi/paste/62bacbbc4f607e2b21a351/

    You are given an array of n integers. You want to modify the array so that 
    it is increasing, i.e., every element is at least as large as the previous 
    element.

    On each move, you may increase the value of any element by one. What is the 
    minimum number of moves required?

    The first input line contains an integer n: the size of the array. Then, 
    the second line contains n integers x1,x2,…,xn: the contents of the array.
    Print the minimum number of moves.

    Constraints: 
    . 1 ≤ n ≤ 2 * 10^5
    . 1 ≤ xi ≤ 10^9
    """
    mov, cur = 0, 0
    for val in arr.split(' '):
        val = int(val)
        if val < cur:
            mov += cur - val
        else:
            cur = val

    return mov


if __name__ == '__main__':
    increasing_array('5', '3 2 5 1 7')
    increasing_array('10', '1 1 1 1 1 1 1 1 1 1')
    increasing_array('10', '6 10 4 10 2 8 9 2 7 7')
''' terminal
run increasing_array('5', '3 2 5 1 7')
got 5 in 0.0000199000 secs.

run increasing_array('10', '1 1 1 1 1 1 1 1 1 1')
got 0 in 0.0000184000 secs.

run increasing_array('10', '6 10 4 10 2 8 9 2 7 7')
got 31 in 0.0000193000 secs.
'''
