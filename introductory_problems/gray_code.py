def gray_code(n: int) -> list[str]:
    """
    [Medium] https://cses.fi/problemset/task/2205
    [Solution] https://cses.fi/paste/571f1fe5c20a194f4b06df/
    [Tutorial] https://www.geeksforgeeks.org/generate-n-bit-gray-codes/

    A Gray code is a list of all 2^n bit strings of length n, where any two 
    successive strings differ in exactly one bit (i.e., their Hamming distance 
    is one).

    Your task is to create a Gray code for a given length n.

    The only input line has an integer n.

    Print 2^n lines that describe the Gray code. You can print any valid 
    solution.

    Constraints:
    1 ≤ n ≤ 16

    Input:
    2

    Output:
    00
    01
    11
    10
    """
    if n == 1:
        return ['0', '1']

    codes = gray_code(n - 1)
    return [f'0{c}' for c in codes] + [f'1{c}' for c in codes[::-1]]


if __name__ == '__main__':
    print(gray_code(2))
    print(gray_code(3))


""" terminal
['00', '01', '11', '10']
['000', '001', '011', '010', '110', '111', '101', '100']
"""
