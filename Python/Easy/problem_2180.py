"""
2180. Count Integers With Even Digit Sum

Given a positive integer num,
return the number of positive integers less than or
equal to num whose digit sums are even.
The digit sum of a positive integer is the sum of all its digits.

Example 1:
    Input: num = 4
    Output: 2
Explanation:
    The only integers less than or equal to 4
    whose digit sums are even are 2 and 4.  

Example 2:
    Input: num = 30
    Output: 14
Explanation:
    The 14 integers less than or equal to 30
    whose digit sums are even are:
    2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
"""

# Solution

class Solution(object):
    def digitSum(self, num):
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
        
    def countEven(self, num):
        counter = 0
        for number in range(1, num+1):
            if self.digitSum(number) % 2 == 0:
                counter += 1
        return counter