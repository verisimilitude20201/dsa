"""
Basic Enclid's algorithm for GCD for two integers p and q.

1. Calculate the remainder of p and q
2. If remainder is 0
    i. return q as the GCD.
3. Set p=q and q=r and go back to step 1 (Recursive call)

For example

1. p = 16, q = 18, r = 16 % 18  = 16
2. Remainder is not 0.
3. p = 18, q = 16, r = 18 % 16 = 2
4. Remainder is not 0.
5. p = 16, q = 2, r = 16 % 2 = 0
6. Remainder is 0, therefore, GCD is value of q in step 6 so 2.

"""


def gcd(p, q):
    r = p % q
    if r == 0:
        return q
    return gcd(q, r)


print(gcd(4, 12))
