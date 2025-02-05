"""
1154. Day of the Year

Given a string date representing a Gregorian calendar date
formatted as YYYY-MM-DD, return the day number of the year.

Example 1:
    Input: date = "2019-01-09"
    Output: 9
Explanation:
    Given date is the 9th day of the year in 2019.

Example 2:
    Input: date = "2019-02-10"
    Output: 41
"""

# Solution

class Solution(object):
    def isLeap(self, year):
        return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

    def dayOfYear(self, date):
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.isLeap(year):
            daysInMonths[1] = 29

        return sum(daysInMonths[:month - 1]) + day