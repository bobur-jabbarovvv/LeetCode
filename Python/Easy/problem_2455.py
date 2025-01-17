"""
2455. Average Value of Even Numbers That Are Divisible by Three

Given an integer array nums of positive integers,
return the average value of all even integers
that are divisible by 3.
Note that the average of n elements is
the sum of the n elements divided by n and
rounded down to the nearest integer.

Example 1:
    Input: nums = [1,3,6,10,12,15]
    Output: 9
Explanation:
    6 and 12 are even numbers that are divisible by 3.
    (6 + 12) / 2 = 9.

Example 2:
    Input: nums = [1,2,4,7,10]
    Output: 0
Explanation:
    There is no single number that satisfies the requirement,
    so return 0.
"""

# Solution

class Solution(object):
    def averageValue(self, nums):
        mylist = []
        for num in nums:
            if num % 6 == 0:
                mylist.append(num)
        if len(mylist) == 0:
            return 0
        else:
            return sum(mylist) // len(mylist)