"""
Approach
--------
KMP
---

For this example, there is no reuse of the pattern, 
T => 
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b


P =>

0   1   2   3   4   5
a   b   a   c   a   b


Fail => List

[0, 0, 1, 0, 1, 2]


Solution

1.  First step


0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
j

0   1   2   3   4   5
a   b   a   c   a   b
k



2. T[j] == P[k], so increment both

0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
    j

0   1   2   3   4   5
a   b   a   c   a   b
    k


3. T[j] == P[k], so increment both

0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
        j

0   1   2   3   4   5
a   b   a   c   a   b
        k


4. T[j] == P[k], so increment both (Skipped 3 steps)

0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
                    j

0   1   2   3   4   5
a   b   a   c   a   b
                    k


5. Now, P[k] and T[j] are not equal, need to reset k. k = fail[k - 1]

Fail => List

[0, 0, 1, 0, 1, 2]. k = fail[5 - 1] = 1


0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
                    j

0   1   2   3   4   5
a   b   a   c   a   b
    k

6. P[k] != T[j],  need to reset k. k = fail[k - 1]


Fail => List

[0, 0, 1, 0, 1, 2]. k = fail[1 - 1] = 0


0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
                    j

0   1   2   3   4   5
a   b   a   c   a   b
k

7. P[k] == T[j] for next 4 characters positions 5 to 8 of the string T

0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
                                    j

0   1   2   3   4   5
a   b   a   c   a   b
                k

8. Again P[k] != T[j], need to reset k, need to reset k. k = fail[k - 1]

Fail => List

[0, 0, 1, 0, 1, 2]. k = fail[4 - 1] = 1

0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
                                    j

0   1   2   3   4   5
a   b   a   c   a   b
    k


9. Again P[k] != T[j], need to reset k, need to reset k. k = fail[k - 1]

Fail => List

[0, 0, 1, 0, 1, 2]. k = fail[1 - 1] = 0

0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
                                        j

0   1   2   3   4   5
a   b   a   c   a   b
k


10.   P[k] = T[j] for the next 6 positons from 10 to 15 in string.
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
a   b   a   c   a   a   b   a   c   c   a   b   a   c   a   b   a   a   b   b
                                                            j

0   1   2   3   4   5
a   b   a   c   a   b
                    k

First index of match is = j - length of pattern + 1 = 10

Complexity
---------
Time: O(m + n)
Space: O(1)
\
"""
def failure_function(P):
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1

    return fail

def find_kmp(T, P):
    n = len(T)
    m = len(P)
    if m == 0:
        return 0
    j = 0
    k = 0
    fail = failure_function(P)
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1

    return -1


T = "abacaabaccabacabaabb"
P = "abacab"

print(find_kmp(T, P))

