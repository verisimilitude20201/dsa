"""
Approach
--------
CS = Current smallest, S  = Smallest

0. [3, 4, 1, 19, 21, 17, 18, 2]  ---> Find current smallest from 1 to N - 1. 3 < 1? Swap
    S     CS


1. [1*, 4, 3, 19, 21, 17, 18, 2]  ---> Find current smallest from 2 to N - 1. 4 < 2? Swap
        S                     CS


1. [1*, 2*, 3, 19, 21, 17, 18, 4]  ---> Find current smallest from 3 to N - 1. Nothing found so continue

Time complexity
--------------
Time: O(N^2)
Space: O(1)

"""
def selection_sort(A):
    for i in range(len(A)):
        current_smallest_index = smallest_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[current_smallest_index]:
                current_smallest_index = j
        if A[current_smallest_index] < A[smallest_index]:
            A[smallest_index], A[current_smallest_index] = A[current_smallest_index], A[smallest_index]