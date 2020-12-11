"""
Boyer-Moore Pattern match

Approach
--------
To improve upon the brute force one, we use two heuristics here.

1. Looking Glass heuristic: Begin comparisons from end of P.
2. Character Jump: If a mismatch occurs within string T such that T[i] is not equal to the P[k], we
need to jump the pattern to the right by few positions.
    i. We first find the index in P that T[i] occurs. Call it j.
    ii. If that index is to the left of the mismatched character, we jump by m - (j + 1) positions to 
    the right. 
    iii. If j is to the left of the mismatched character we jump by m - k positions to the right.
    iv. We use a hash table to store the characters of P as key and their indexes as values to aid 
    an O(1) lookup
    v. If there is not a mismatched character, we try to align the P and S character by character from the
    end of P..

Complexity
----------
Time: O(n + m + Number of distinct alphabets). n and m are the length of the target string and pattern

"""

def find_string_by_boyer_moore(P, S):
    pattern_length = len(P)
    string_length = len(S)
    last = {}
    for k in range(pattern_length):
        last[P[k]] = k

    i = pattern_length - 1
    k = pattern_length - 1
    while i < string_length:
        if S[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(S[i], -1)
            i += pattern_length - min(k, j + 1)
            k = pattern_length - 1


print(find_string_by_boyer_moore("iji", "Abhijit"))