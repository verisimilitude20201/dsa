"""
This determines if a given number is prime or not.

Basic algorithm
--------------

Let n be the number which we want to find if its a prime or not. By number theory, following axiom holds good.

1. O and 1 are neither prime nor composite numbers.
2. If a number is prime, it has only two divisors, 1 and itself.
3. To check if n is prime, we loop from 2 to a number that's less than the square root of n. Check if any number divides n perfectly. If not, its a prime number.

"""


import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


print(is_prime(10))

print(is_prime(2))

print(is_prime(19))

print(is_prime(21))