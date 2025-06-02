"""
989. Add to Array-Form of Integer

The array-form of an integer num
is an array representing its digits in left to right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k,
return the array-form of the integer num + k.

Example 1:
    Input: num = [1,2,0,0], k = 34
    Output: [1,2,3,4]
Explanation:
    1200 + 34 = 1234

Example 2:
    Input: num = [2,7,4], k = 181
    Output: [4,5,5]
Explanation:
    274 + 181 = 455

Example 3:
    Input: num = [2,1,5], k = 806
    Output: [1,0,2,1]
Explanation:
    215 + 806 = 1021
"""

# Solution

class Solution(object):
    def addToArrayForm(self, num, k):
        n = 0
        numList = []

        for i in range(len(num)):
            n += num[len(num) - 1 - i] * (10 ** i)
        
        total = n + k

        while total > 0:
            digit = total % 10 # Get the last digit
            numList.insert(0, digit) # Add it at the start of the list
            total //= 10 # Remove the last digit
            
        return numList