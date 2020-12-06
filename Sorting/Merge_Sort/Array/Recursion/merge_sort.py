"""
Approach
--------
1. Recursively divide the list into two sub-lists till the length of the lists is less than 2. 
2. Sort each list and merge them.


Complexity
Time: O(N * log(N)) For splitting into half time is O(log N), and for merging the time is O(N). 
Space: 
"""
def merge_sort(A):
    n = len(A)
    if n < 2:
        return
    mid = n // 2
    S1 = A[0:mid]
    S2 = A[mid:n]
    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, A)


def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1


L = [29, 10, 44, 33, 2, 3, 39, 31]
merge_sort(L)
print(L)