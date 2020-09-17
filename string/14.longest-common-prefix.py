#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        ans = strs[0]
        for x in strs[1:]:
            while not x.startswith(ans):
                ans = ans[:-1]
        return ans

