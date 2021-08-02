#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (60.84%)
# Likes:    5849
# Dislikes: 275
# Total Accepted:    903.9K
# Total Submissions: 1.5M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#
import unittest
from typing import List


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore Voting Algorithm."""
        counter, majority_num = 0, 0
        for num in nums:
            if counter == 0:  # switch majority num
                counter += 1
                majority_num = num
            elif majority_num == num:
                counter += 1
            else:
                counter -= 1
        return majority_num


# @lc code=end


class HashmapSolution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1

        max_count, majority_num = 1, 0
        for num, num_count in res.items():
            if num_count > max_count:
                max_count = num_count
                majority_num = num
        return majority_num


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().majorityElement

    def test_example1(self):
        self.assertEqual(self.s([3, 2, 3]), 3)

    def test_example2(self):
        self.assertEqual(self.s([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
