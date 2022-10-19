def draw(mat: list[list[int]], queens) -> None:
    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            if (i, j) in queens:
                print('Q'.ljust(3), end=' ')
            else:
                print(f'{col: <3}', end=' ')
        print()
    print()


def can_attack(old_queen: tuple[int, int], new_queen: tuple[int, int]) -> bool:
    delta_x, delta_y = new_queen[0] - old_queen[0], new_queen[1] - old_queen[1]
    return not delta_x or not delta_y or abs(delta_x) == abs(delta_y)


def chessboard_and_queens(board, queens, row_id) -> int:
    """
    [Medium] https://cses.fi/problemset/task/1624
    [Solution] https://cses.fi/paste/594387c5a44df80649c203/

    Your task is to place eight queens on a chessboard so that no two queens 
    are attacking each other. As an additional challenge, each square is either 
    free or reserved, and you can only place queens on the free squares. 
    However, the reserved squares do not prevent queens from attacking each 
    other.

    How many possible ways are there to place the queens?

    The input has eight lines, and each of them has eight characters. Each square is either free (.) or reserved (*).

    Print one integer: the number of ways you can place the queens.

    Input:
    . . . . . . . .
    . . . . . . . .
    . . * . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . * * .
    . . . * . . . .
    . . . . . . . .

    Output:
    65
    """
    if row_id == len(board):
        draw(board, queens)  # we have a solution
        return 1

    count = 0
    for col_id, sym in enumerate(board[row_id]):
        if sym == "*":
            continue

        cur = (row_id, col_id)
        # check if any of the previous queens can attack the current position
        if any(can_attack(pos, cur) for pos in queens):
            continue

        # if a queen can be safely placed in the current row, add its position
        queens.append(cur)
        # recursively call the function and place another queen on the next row
        count += chessboard_and_queens(board, queens, row_id + 1)
        # remove queen from current position, to test another position on the
        # same row
        queens.pop()

    return count


if __name__ == '__main__':
    board = '''
    . . . . . .
    . . . . . .
    . . * . . .
    . . . . . .
    . . . . . .
    . . . . . *
    '''.strip().split('\n')
    board = [row.strip().split(' ') for row in board]
    print(chessboard_and_queens(board, [], 0))


""" terminal
.   Q   .   .   .   .   
.   .   .   Q   .   .   
.   .   *   .   .   Q   
Q   .   .   .   .   .   
.   .   Q   .   .   .   
.   .   .   .   Q   *   

.   .   Q   .   .   .   
.   .   .   .   .   Q   
.   Q   *   .   .   .   
.   .   .   .   Q   .   
Q   .   .   .   .   .   
.   .   .   Q   .   *   

.   .   .   Q   .   .   
Q   .   .   .   .   .   
.   .   *   .   Q   .   
.   Q   .   .   .   .   
.   .   .   .   .   Q   
.   .   Q   .   .   *   

.   .   .   .   Q   .   
.   .   Q   .   .   .   
Q   .   *   .   .   .   
.   .   .   .   .   Q   
.   .   .   Q   .   .   
.   Q   .   .   .   *   

4
"""
