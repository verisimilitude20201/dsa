"""
Approach
--------
Pass 0: 0 to N - 1
0 [3, 4, 1, 19, 21, 17, 18, 2]      # Compare 3 and 4, 3 < 4 so don't swap
1 [3, 1, 4, 19, 21, 17, 18, 2]      # Compare 4 and 1, 4 < 1 so swap 
2 [3, 1, 4, 19, 21, 17, 18, 2]      # Compare 4 and 19, 4 < 19 so don't swap 
3 [3, 1, 4, 19, 21, 17, 18, 2]      # Compare 19 and 21, 19 < 21 so don't swap 
4 [3, 1, 4, 19, 17, 21, 18, 2]      # Compare 17 and 21, 21 < 17 so swap
5 [3, 1, 4, 19, 17, 18, 21, 2]      # Compare 21 and 18, 21 < 18 so swap 
6 [3, 1, 4, 19, 17, 18, 2, 21*]     # Compare 21 and 2, 21 < 2 so swap, now 21 is largest element and is fixed.

Pass 1: 0 to N - 2
7 [1, 3, 4, 19, 17, 18, 2, 21*]     # Compare 3 and 1, 3 < 1 so swap
8 [1, 3, 4, 19, 17, 18, 2, 21*]     # Compare 3 and 4, 3 < 4 so don't swap
9 [1, 3, 4, 19, 17, 18, 2, 21*]     # Compare 4 and 19, 4 < 19 so don't swap
10 [1, 3, 4, 17, 19, 18, 2, 21*]     # Compare 19 and 17, 19 < 17 so swap
11 [1, 3, 4, 17, 18, 19, 2, 21*]     # Compare 19 and 18, 19 < 18 so swap
12 [1, 3, 4, 17, 18, 2, 19*, 21*]    # Compare 19 and 2, 19 < 2 so swap, now 19 is second-largest element and is fixed.

Pass 2: 0 to N - 3
13 [1, 3, 4, 17, 18, 2, 19*, 21*]    # Compare 1 and 3, 1 < 3 so don't swap
14 [1, 3, 4, 17, 18, 2, 19*, 21*]    # Compare 3 and 4, 3 < 4 so don't swap
15 [1, 3, 4, 17, 18, 2, 19*, 21*]    # Compare 4 and 17, 4 < 17 so don't swap
16 [1, 3, 4, 17, 18, 2, 19*, 21*]    # Compare 17 and 18, 17 < 18 so don't swap
17 [1, 3, 4, 17, 2, 18*, 19*, 21*]   # Compare 18 and 2, 18 < 2 so swap, now 18 is third-largest element and is fixed.

Pass 3: 0 to N - 4
18 [1, 3, 4, 17, 2, 18*, 19*, 21*]   # Compare 1 and 3, 1 < 3 so don't swap
19 [1, 3, 4, 17, 2, 18*, 19*, 21*]   # Compare 3 and 4, 3 < 4 so don't swap
20 [1, 3, 4, 17, 2, 18*, 19*, 21*]   # Compare 4 and 17, 4 < 17 so don't swap
21 [1, 3, 4, 2, 17*, 18*, 19*, 21*]   # Compare 17 and 2, 17 < 2 so swap, 17 is the fourth largest number and is fixed

Pass 4: 0 to N - 5
21 [1, 3, 4, 2, 17*, 18*, 19*, 21*]   # Compare 1 and 3, 1 < 3 so dont swap
22 [1, 3, 4, 2, 17*, 18*, 19*, 21*]   # Compare 3 and 4, 3 < 4 so dont swap
23 [1, 3, 2, 4*, 17*, 18*, 19*, 21*]   # Compare 4 and 2, 4 < 2 so swap, 4 is the fifth largest number and is fixed

Pass 5: 0 to N - 6
24 [1, 3, 2, 4*, 17*, 18*, 19*, 21*]   # Compare 1 and 3, 1 < 3 so don't swap
25 [1, 2, 3*, 4*, 17*, 18*, 19*, 21*]   # Compare 1 and 3, 3 < 2 so swap, 3 is the sixth largest number and is fixed

Pass 6: 0 to N - 7
26 [1*, 2*, 3*, 4*, 17*, 18*, 19*, 21*]   # Compare 1 and 3, 1 < 3 so don't swap, 1 and 3 are also fixed now.

Time complexity
--------------
Time: O(N^2)
Space: O(1)


"""
def bubble_sort(A):
    current_pass = 1
    i = 0
    N = len(A)
    while i < N - current_pass:
        for j in range(N - current_pass):
            if A[j] >= A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
        current_pass += 1


A = [3, 4, 1, 19, 21, 17, 18, 2]
bubble_sort(A)
print(A)