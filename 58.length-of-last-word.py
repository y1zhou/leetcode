#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        ans = 0
        for x in s.rstrip()[::-1]:
            if x == " ":
                break
            ans += 1

        return ans

