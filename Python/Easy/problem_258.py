"""
258. Add Digits

Given an integer num,
repeatedly add all its digits until the result has only one digit,
and return it.

Example 1:
    Input: num = 38
    Output: 2
Explanation:
    The process is:
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2 
    Since 2 has only one digit, return it.

Example 2:
    Input: num = 0
    Output: 0
"""

# Solution

class Solution(object):
    def addDigits(self, num):
        if (len(str(num)) != 1):
            sum = 0
            for digit in str(num):
                sum += int(digit)
            return self.addDigits(sum)
        else:
            return num