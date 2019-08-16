#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]
