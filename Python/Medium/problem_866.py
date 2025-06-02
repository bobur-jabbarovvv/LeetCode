"""
866. Prime Palindrome

Given an integer n,
return the smallest prime palindrome greater than or equal to n.
An integer is prime if it has exactly two divisors:
-1 and itself. Note that 1 is not a prime number.

For example, 2, 3, 5, 7, 11, and 13 are all primes.
An integer is a palindrome
if it reads the same from left to right as it does from right to left.

For example, 101 and 12321 are palindromes.
The test cases are generated so that the answer always exists
and is in the range [2, 2 * 108].

Example 1:
    Input: n = 6
    Output: 7

Example 2:
    Input: n = 8
    Output: 11

Example 3:
    Input: n = 13
    Output: 101
"""

# Solution

class Solution(object):
    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def isPalindrome(self, n):
        s = str(n)
        return s == s[::-1]

    def primePalindrome(self, n):
        # Palindromes with even length > 11 are divisible by 11 and thus not prime
        while True:
            if self.isPalindrome(n) and self.isPrime(n):
                return n
            # Optimization: skip even numbers > 2
            if n > 11 and len(str(n)) % 2 == 0:
                n = 10 ** len(str(n)) + 1
            else:
                n += 1