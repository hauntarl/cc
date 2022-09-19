from util import timeit
from math import sqrt, pow

sqrt5 = sqrt(5)


@timeit
def fibonacci(n: int) -> int:
    """
    There is a closed-form formula for calculating Fibonacci numbers, which is 
    sometimes called Binet’s formula.
    f(n) = ((1 + √5)^n - (1 - √5)^n) / (2^n * √5)
    """
    if n < 1:
        return 0

    num1 = pow(1 + sqrt5, n)
    num2 = pow(1 - sqrt5, n)
    den1 = pow(2, n)
    return round((num1 - num2) / (den1 * sqrt5))


# print the first 11 fibonacci numbers
[fibonacci(n) for n in range(11)]
''' terminal
run fibonacci(0)
got '0' in 0.0000054000 secs.

run fibonacci(1)
got '1' in 0.0000920000 secs.

run fibonacci(2)
got '1' in 0.0000246000 secs.

run fibonacci(3)
got '2' in 0.0000230000 secs.

run fibonacci(4)
got '3' in 0.0000162000 secs.

run fibonacci(5)
got '5' in 0.0000521000 secs.

run fibonacci(6)
got '8' in 0.0001299000 secs.

run fibonacci(7)
got '13' in 0.0000853000 secs.

run fibonacci(8)
got '21' in 0.0000172000 secs.

run fibonacci(9)
got '34' in 0.0000311000 secs.

run fibonacci(10)
got '55' in 0.0000254000 secs.
'''
