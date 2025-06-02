"""
1812. Determine Color of a Chessboard Square

You are given coordinates,
a string that represents the coordinates of a square of the chessboard.

Return true if the square is white,
and false if the square is black.
The coordinate will always represent a valid chessboard square.
The coordinate will always have the letter first, and the number second.

Example 1:
    Input: coordinates = "a1"
    Output: false
Explanation:
    The square with coordinates "a1" is black,
    so return false.

Example 2:
    Input: coordinates = "h3"
    Output: true
Explanation:
    The square with coordinates "h3" is white,
    so return true.

Example 3:
    Input: coordinates = "c7"
    Output: false
"""

# Solution

class Solution(object):
    def squareIsWhite(self, coordinates):
        # List of columns where the first row is white
        ws = ['b', 'd', 'f', 'h']
        # Check if the column is in the list 'ws'
        if coordinates[0] in ws:
            # If the row number is odd
            if int(coordinates[1]) % 2 != 0:
                # The square is white
                return True
        # If the column is not in 'ws' and the row number is even
        else:
            if int(coordinates[1]) % 2 == 0:
                # The square is white
                return True
        # If the square is not white
        return False