"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

# Solution

class Solution(object):
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return x * self.pow(x, n-1)

    def binaryToDecimal(self, x):
        result = 0
        for i, char in enumerate(reversed(x)):
            if char == "1":
                result = result + self.pow(2, i)
        return result

    def decimalToBinary(self, x):
        if x == 0:
            return "0"
        binary = ""
        while (x > 0):
            binary = str(x % 2) + binary
            x = x // 2
        return binary

    def addBinary(self, a, b):
        aDecimal = self.binaryToDecimal(a)
        bDecimal = self.binaryToDecimal(b)
        result = self.decimalToBinary(aDecimal + bDecimal)
        return result