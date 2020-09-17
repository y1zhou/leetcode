#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if all([x < 0 for x in nums]):
            return max(nums)
        running_sum = 0
        ans = 0
        for x in nums:
            running_sum += x
            if running_sum < 0:
                running_sum = 0
                continue
            if ans < running_sum:
                ans = running_sum
        return ans
