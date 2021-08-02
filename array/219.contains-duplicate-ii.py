#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (39.60%)
# Likes:    1549
# Dislikes: 1497
# Total Accepted:    359.1K
# Total Submissions: 906K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#
import unittest
from typing import List


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = {}
        for i, val in enumerate(nums):
            if val in counter and i - counter[val] <= k:
                return True
            counter[val] = i
        return False

    # @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().containsNearbyDuplicate

    def test_example1(self):
        self.assertEqual(self.s([1, 2, 3, 1], 3), True)

    def test_example2(self):
        self.assertEqual(self.s([1, 0, 1, 1], 1), True)

    def test_example3(self):
        self.assertEqual(self.s([1, 2, 3, 1, 2, 3], 2), False)


if __name__ == "__main__":
    unittest.main()
