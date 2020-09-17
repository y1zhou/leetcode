#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)

        while i < j:
            if nums[i] == val:
                j -= 1
                nums[i] = nums[j]
            else:
                i += 1

        return i

