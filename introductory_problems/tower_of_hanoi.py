def tower_of_hanoi(n: int, beg: int, end: int, aux: int) -> list[int]:
    """
    [Easy] https://cses.fi/problemset/task/2165
    [Solution] https://cses.fi/paste/706cadc2711c2a6e4ae1ee/
    [Tutorial] https://www.youtube.com/watch?v=YstLjLCGmgg

    The Tower of Hanoi game consists of three stacks (left, middle and right) 
    and n round disks of different sizes. Initially, the left stack has all the 
    disks, in increasing order of size from top to bottom.

    The goal is to move all the disks to the right stack using the middle stack.
    On each move you can move the uppermost disk from a stack to another stack. 
    In addition, it is not allowed to place a larger disk on a smaller disk.

    Your task is to find a solution that minimizes the number of moves.

    The only input line has an integer n: the number of disks.

    First print an integer k: the minimum number of moves.

    After this, print k lines that describe the moves. Each line has two 
    integers a and b: you move a disk from stack a to stack b.

    Constraints:
    1 ≤ n ≤ 16

    Input:
    2

    Output:
    3
    1 2
    1 3
    2 3
    """
    if n == 1:
        return [(beg, end)]

    steps = []
    steps.extend(tower_of_hanoi(n - 1, beg, aux, end))
    steps.append((beg, end))
    steps.extend(tower_of_hanoi(n - 1, aux, end, beg))
    return steps


if __name__ == '__main__':
    for step in tower_of_hanoi(3, 1, 3, 2):
        print(step)


""" terminal
(1, 3)
(1, 2)
(3, 2)
(1, 3)
(2, 1)
(2, 3)
(1, 3)
"""
