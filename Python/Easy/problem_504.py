"""
504. Base 7

Given an integer num,
return a string of its base 7 representation.

Example 1:
    Input: num = 100
    Output: "202"

Example 2:
    Input: num = -7
    Output: "-10"
"""

# Solution

class Solution(object):
    def convertToBase7(self, num):
        if num < 0:
            return "-" + self.convertToBase7(-num)
        elif num == 0:
            return "0"
            
        result = ""
        while (num>0):
            result = str(num % 7) + result
            num //= 7

        return result