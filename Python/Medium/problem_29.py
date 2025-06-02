"""
29. Divide Two Integers

Given two integers dividend and divisor,
divide two integers without using multiplication,
division, and mod operator.
The integer division should truncate toward zero,
which means losing its fractional part.
For example, 8.345 would be truncated to 8,
and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment
that could only store integers within the 32-bit signed integer range:
[-2^31, 2^31 - 1]. For this problem, if the quotient is strictly greater than 231 - 1,
then return 2^31 - 1, and if the quotient is strictly less than -231,
then return -2^31.

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
Explanation:
    10/3 = 3.33333.. which is truncated to 3.

Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
Explanation:
    7/-3 = -2.33333.. which is truncated to -2.
"""

# Solution

class Solution(object):
    def divide(self, dividend, divisor):
        # Define 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case: if dividend is INT_MIN and divisor is -1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Handle trivial cases for optimization
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend

        # Determine the sign of the quotient
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with absolute values for easier calculation
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Optimized subtraction using exponential search
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1

            # Double the divisor using addition (instead of bit manipulation)
            while dividend >= temp_divisor + temp_divisor:
                temp_divisor += temp_divisor
                multiple += multiple

            # Subtract the largest found divisor from dividend
            dividend -= temp_divisor
            quotient += multiple

        # Apply the sign to the quotient
        quotient = quotient if sign > 0 else -quotient

        # Ensure the result is within the 32-bit signed integer range
        if quotient < INT_MIN:
            return INT_MIN
        elif quotient > INT_MAX:
            return INT_MAX
        else:
            return quotient