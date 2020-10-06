"""
Basic algorithm
---------------------
Consider,

A = Array containing i elements.
N = size of array.

1. for i = 0 to floor(N/2)
    1.1. Swap ith and (N - i - 1)st element

"""

def max_element(A):
    maximum = -99
    for i in range(0, len(A)):
        if A[i] > maximum:
            maximum = A[i]
    return maximum


print(max_element([56, 77, 88, 90, 91, 91, 92]))
