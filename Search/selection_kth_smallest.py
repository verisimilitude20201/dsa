"""
Approach
--------
Kth smallest element
--------------------

[30, 10, 34, 11, 2, 3, 8, 17] Find 5th Smallest element

1. Find random pivot

[30, 10, 34, 11, 2, 3, 8, 17]
              P


2. L = [2, 3, 8, 10]
   E  = [11]
   G = [17, 30, 34]

3. 11 ?

-------------------------------------------------------------------------------
Find 7th Smallest element

1. Find random pivot

[30, 10, 34, 11, 2, 3, 8, 17]
                       P             
 
2. 

   L = [2, 3]
   E  = [8]
   G = [10, 17, 30, 34]

4. Sequence reduces to S = [10, 17, 30, 34] and k = 4
                                         P

   L = [10, 17, 30]
   E  = [34]
   G = []

5. Sequence now reduces to S = [10, 17, 30] and k = 4
                                P


6. L = []
   E = [10]
   G = [17, 30] 

7. Sequence now reduces to S = [17, 30] and k = 3
                                P 

8. L = []
   E = [17]
   G = [30]

9. 30..

Complexity
---------
Time: O(N)
Space: O(N + n): For N is the total length of the 3 auxillary arrays and n is the number of recursive calls.

"""
def randomized_quick_select(S, k):
    if len(S) == 1:
        return S[0]

    pivot = random.choice(S)
    L = [x for x in S if x < pivot]
    E = [x for x in S if x == pivot]
    G = [x for x in S if x > pivot]
    if k <= len(L):
        return randomized_quick_select(L, k)
    elif k <= len(L) + len(E):
        return pivot
    else:
        return randomized_quick_select(G, k - len(L) - len(E))