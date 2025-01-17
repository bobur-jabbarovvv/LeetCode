"""
231. Power of Two

Description
Given an integer n, return true if it is a power of two.
Otherwise, return false.
An integer n is a power of two,
if there exists an integer x such that n == 2x.

Example 1:
    Input: n = 1
    Output: true
Explanation:
    2^0 = 1

Example 2:
    Input: n = 16
    Output: true
Explanation:
    2^4 = 16

Example 3:
    Input: n = 3
    Output: false

"""

class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        elif n == 1:
            return True
        elif n % 2 == 0:
            return self.isPowerOfTwo(n // 2)
        else:
            return False
