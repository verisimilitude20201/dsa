"""
Approach
----------

Outer loop assumes that each character in the target string is the starting character pattern to be found.
Inner Loop goes through the string and tries to find the pattern.


Complexity:
----------- 
Time: O(mn) m is the number of characters in pattern, n is the length of the target string.
Space: O(1)
"""

def find_string_by_brute_force(P, S):
    pattern_length = len(P)
    string_length = len(S)
    if pattern_length > string_length:
        return -1
    for i in range(pattern_length + 1):
        j = i
        while j < pattern_length and S[i + j] == P[j]:
            j += 1
        if j == pattern_length:
            return i

    return -1


print(find_string_by_brute_force("hi", "Abhijit"))