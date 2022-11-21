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
- *[largest_common_subsequence.py](https://github.com/hauntarl/cc/blob/main/largest_common_subsequence.py)*

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

### Sorting

There are many algorithms for sorting, and they are also good examples of how to apply different algorithm design techniques. The efficient general sorting algorithms work in `O(n logn)` time, and many algorithms that use sorting as a subroutine also have this time complexity.

The lower bound `nlogn` does not apply to algorithms that do not compare array elements but use some other information. An example of such an algorithm is **counting sort** that sorts an array in `O(n)` time assuming that every element in the array is an integer between `0... c` and `c = O(n)`.
The algorithm creates a bookkeeping array, whose indices are elements of the original array. The algorithm iterates through the original array and calculates how many times each element appears in the array.

### Searching

A general method for searching for an element in an array is to use a for loop that iterates through the elements of the array.
The time complexity of this approach is `O(n)`, because in the worst case, it is necessary to check all elements of the array. If the order of the elements is arbitrary, this is also the best possible approach, because there is no additional information available where in the array we should search for the element `x`.

However, if the array is sorted, the situation is different. In this case it is possible to perform the search much faster, because the order of the elements in the array guides the search. The binary search algorithm efficiently searches for an element in a sorted array in `O(logn)` time.

#### Alternate Binary Search

``` python
def search(arr, x):
    i, k = len(arr) // 2, 0
    while i > 0:
        while i + k < len(arr) and arr[i + k] <= x:
            k += i
        i //= 2
    
    return k if arr[k] == x else -1
```
