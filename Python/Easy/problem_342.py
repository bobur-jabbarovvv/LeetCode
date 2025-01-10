"""
342. Power of Four

Given an integer n, return true if it is a power of four.
Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
    Input: n = 16
    Output: true

Example 2:
    Input: n = 5
    Output: false

Example 3:
    Input: n = 1
    Output: true
"""

# Solution

class Solution(object):
    def isPowerOfFour(self, n):
        if n < 1:
            return False
        elif n == 1:
            return True
        elif n % 4 == 0:
            return self.isPowerOfFour(n // 4)
        else:
            return False
