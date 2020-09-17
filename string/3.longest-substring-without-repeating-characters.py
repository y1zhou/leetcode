#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        uniqChars = ""
        for i in range(len(s)):
            if s[i] in uniqChars:
                prevPos = uniqChars.find(s[i])
                uniqChars = uniqChars[prevPos + 1 :]
            uniqChars += s[i]
            maxLength = max(maxLength, len(uniqChars))
        return maxLength

