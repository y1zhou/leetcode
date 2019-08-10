#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen = len(needle)
        if needleLen == 0:
            return 0
        for i in range(len(haystack) - needleLen + 1):
            if haystack[i : i + needleLen] == needle:
                return i

        return -1
