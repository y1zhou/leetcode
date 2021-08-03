#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (30.82%)
# Likes:    1192
# Dislikes: 1934
# Total Accepted:    251.6K
# Total Submissions: 815.7K
# Testcase Example:  '[3,2,1]'
#
# Given integer array nums, return the third maximum number in this array. If
# the third maximum does not exist, return the maximum number.
#
#
# Example 1:
#
#
# Input: nums = [3,2,1]
# Output: 1
# Explanation: The third maximum is 1.
#
#
# Example 2:
#
#
# Input: nums = [1,2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
#
#
# Example 3:
#
#
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Can you find an O(n) solution?
#
import unittest
from typing import List


# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = [float("-inf")] * 3
        for num in nums:
            if num in max_nums:
                continue
            if num > max_nums[0]:
                max_nums = [num, max_nums[0], max_nums[1]]
            elif num > max_nums[1]:
                max_nums = [max_nums[0], num, max_nums[1]]
            elif num > max_nums[2]:
                max_nums[2] = num

        if float("-inf") in max_nums:
            return max_nums[0]
        else:
            return max_nums[2]


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().thirdMax

    def test_example1(self):
        self.assertEqual(self.s([3, 2, 1]), 1)

    def test_example2(self):
        self.assertEqual(self.s([1, 2]), 2)

    def test_example3(self):
        self.assertEqual(self.s([2, 2, 3, 1]), 1)


if __name__ == "__main__":
    unittest.main()
