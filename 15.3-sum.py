#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        numsLen = len(nums)
        if numsLen < 3:
            return ans
        nums.sort()
        for i in range(0, numsLen - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, numsLen - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    while k > j and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif tmp < 0:
                    j += 1
                else:
                    k -= 1

        return ans
