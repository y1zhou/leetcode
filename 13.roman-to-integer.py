#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        nextChar = "a"
        for c in s[::-1]:
            ans += romanMap[c]
            if c == "I" and (nextChar in "VX"):
                ans -= 2
            elif c == "X" and (nextChar in "LC"):
                ans -= 20
            elif c == "C" and (nextChar in "DM"):
                ans -= 200
            nextChar = c
        return ans
