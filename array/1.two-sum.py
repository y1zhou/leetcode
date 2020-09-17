#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, x in enumerate(nums):
            if target - x in ans.keys():
                return [ans[target - x], i]
            else:
                ans[x] = i
