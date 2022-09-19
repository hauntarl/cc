# Competitive Programming

The CSES Problem Set is a collection of algorithmic programming problems. Refer [Introduction](https://cses.fi/problemset/text/2433) for more details. This repository contains solutions in Python for the mentioned problem set.

If you are new to competitive programming or need a thorough introduction to the basic concepts, terminologies and algorithms. Refer [Competitive Programmer’s Handbook](https://cses.fi/book/book.pdf) by *Antti Laaksonen*. It is a free online book which goes hand in hand with the CSES Problem Set.

>All the benchmarks are generated using [PyPy - Python Interpreter](https://realpython.com/pypy-faster-python/) with the help of *[util.py](https://github.com/hauntarl/cc/blob/main/util.py)*

## Resources

- CSES [Problem Set](https://cses.fi/problemset/)
- Competitive programming [books](https://cses.fi/book/index.php)

## Examples

- *[fibonacci.py](https://github.com/hauntarl/cc/blob/main/fibonacci.py)*
- *[max_subarray_sum.py](https://github.com/hauntarl/cc/blob/main/max_subarray_sum.py)*

### Time Complexity - Estimating efficiency

By calculating the time complexity of an algorithm, it is possible to check, before
implementing the algorithm, that it is efficient enough for the problem. The
starting point for estimations is the fact that a modern computer can perform
some hundreds of millions of operations in a second.

For example, assume that the time limit for a problem is one second and the input size is `n = 10^5`. If the time complexity is `O(n^2)`, the algorithm will perform about `(10^5)^2 = 10^10` operations. This should take at least some **tens of seconds**, so the algorithm seems to be too slow for solving the problem.

On the other hand, given the input size, we can try to guess the required time
complexity of the algorithm that solves the problem. The following table contains
some useful estimates assuming a **time limit of one second**.

Input size | Required time complexity
---------- | ------------------------
`n ≤ 10` | O(n!)
`n ≤ 20` | O(2^n)
`n ≤ 500` | O(n^3)
`n ≤ 5000` | O(n^2)
`n ≤ 10^6` | O(n log n) or O(n)
`n is large` | O(1) or O(log n)
