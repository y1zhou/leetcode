#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (57.82%)
# Likes:    2016
# Dislikes: 864
# Total Accepted:    885.2K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,1]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#
import unittest
from typing import List


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_values = set()
        for num in nums:
            if num in seen_values:
                return True
            seen_values.add(num)
        return False


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().containsDuplicate

    def test_example1(self):
        self.assertEqual(self.s([1, 2, 3, 1]), True)

    def test_example2(self):
        self.assertEqual(self.s([1, 2, 3, 4]), False)

    def test_example3(self):
        self.assertEqual(self.s([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == "__main__":
    unittest.main()
