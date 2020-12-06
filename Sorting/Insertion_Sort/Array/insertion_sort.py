"""
Approach
-------
1. Input

0 1 2 3
4 3 1 2



2. 

current = 4
j = 1


0 	1 	2 3
4 	3 	1 2
    cur
    j

3. j > 0 and A[j - 1] > cur

Set A[j] = A[j - 1] and decrement j

0 	1 	2 3
4 	4 	1 2
j  cur


4. Set A[j] = current

0 	1 	2 3
3 	4 	1 2
j  cur

Time complexity
--------------
Time O(N^2) Where N is the number of elements
Space O(1) No auxillary space.

"""
def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        j = i
        current = sequence[i]
        while j > 0 and sequence[j - 1] > current:
            sequence[j] = sequence[j - 1]
            j -= 1
        sequence[j] = current

    return sequence


print(insertion_sort([3, 1, 4, 2]))