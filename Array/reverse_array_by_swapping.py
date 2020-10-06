"""
Basic algorithm
---------------------
Consider,

A = Array containing i elements.
N = size of array.

1. for i = 0 to floor(N/2)
    1.1. Swap ith and (N - i - 1)st element


Example:
------------
    A = [1, 2, 3, 4]
    N = 4
1. Loop 0:  0th element will be swapped with (N-i-1) i.e. 3rd element

    A = [4, 2, 3, 1]

2. Loop 1:  1st element will be swapped with 2nd element

A = [4, 3, 2, 1]

"""

import math


def reverse(A):
    for i in range(0, math.floor(len(A) / 2)):
        swap_var = A[i]
        A[i] = A[len(A) - i - 1]
        A[len(A) - i - 1] = swap_var

    return A


print(reverse([1, 2, 3, 4]))
print(reverse([1, 2, 3, 4, 5]))
