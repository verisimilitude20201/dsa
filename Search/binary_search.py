"""
This describes the binary search algorithm for searching integers in a list

Basic algorithm
--------------

1. Consider A is an array of size N and we need to find x in it.
2. Further assume that A is sorted in ascending order


I. Consider two pointers that point to the 0th and the last index of array
    low := 0
    high := index of last element in A

II. while low <= high
    a. Compute mid as the middle index of the array.
    b. If A[mid] == x, mid is the position of the element. Return it.
    c. Else If x > A[mid],
        element must be in upper half of the array
        low := mid + 1
        Go to step II.
    d. Else Element must be in lower half of the array.
        high := mid - 1
        Go to step II.

III. Return -1 as the element is not found.

"""


import math


def binary_search(arr, x):
    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = math.floor((low + high) / 2)
        if x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
        else:
            return mid

    return -1


# Find middle number
print(binary_search([10, 12, 14, 15, 17, 20, 22, 23, 24], 17))

# Find last number
print(binary_search([10, 12, 14, 15, 17, 20, 22, 23, 24], 24))

# Find missing number
print(binary_search([10, 12, 14, 15, 17, 20, 22, 23, 24], 25))


# Find left number
print(binary_search([10, 12, 14, 15, 17, 20, 22, 23, 24], 15))

# Find left number
print(binary_search([10, 12, 14, 15, 17, 20, 22, 23, 24], 11))


