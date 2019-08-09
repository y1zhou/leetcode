#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_len = len(nums)
        if num_len <= 1:
            return num_len

        i = 0
        for j in range(1, num_len):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
