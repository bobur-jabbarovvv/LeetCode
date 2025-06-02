"""
242. Valid Anagram

Given two strings s and t,
return true if t is an anagramof s,
and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false
"""

# Solution

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
