#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calcSize(i, j, vi, vj):
            return (j - i) * min(vi, vj)

        biggest_container = 0
        i, j = 0, len(height) - 1
        while i < j:
            biggest_container = max(
                biggest_container, calcSize(i, j, height[i], height[j])
            )
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return biggest_container

