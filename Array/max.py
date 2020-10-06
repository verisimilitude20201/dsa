"""
Basic algorithm
---------------------
1. Set maximum to lowest possible value
2. Iterate through array.
3. If array_element > maximum
    3.1 maximum := array_element
    3.2 Go to 2.
4. Return the last value of maximum

It will contain the largest element in the array

"""

def max_element(A):
    maximum = -99
    for i in range(0, len(A)):
        if A[i] > maximum:
            maximum = A[i]
    return maximum


print(max_element([56, 77, 88, 90, 91, 91, 92]))
