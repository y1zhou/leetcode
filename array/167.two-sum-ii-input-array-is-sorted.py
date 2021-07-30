#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (56.39%)
# Likes:    3066
# Dislikes: 760
# Total Accepted:    617.7K
# Total Submissions: 1.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers numbers that is already sorted in non-decreasing
# order, find two numbers such that they add up to a specific target number.
#
# Return the indices of the two numbers (1-indexed) as an integer array answer
# of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
#
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
#
#
# Example 1:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#
#
# Example 2:
#
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
#
#
# Example 3:
#
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
#
#
#
# Constraints:
#
#
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
#
#
#
import unittest
from bisect import bisect_left
from typing import List


# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i != j:
            ans = numbers[i] + numbers[j]
            if ans == target:
                return [i + 1, j + 1]
            if ans < target:
                i += 1
            else:
                j -= 1


# @lc code=end


class BinarySearchSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            target_num = target - num
            idx = bisect_left(numbers, target_num)
            if numbers[idx] == target_num:
                return [i + 1, idx + 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().twoSum

    def test_example1(self):
        self.assertEqual(self.s(numbers=[2, 7, 11, 15], target=9), [1, 2])

    def test_example2(self):
        self.assertEqual(self.s(numbers=[2, 3, 4], target=6), [1, 3])


def test_example3(self):
    self.assertEqual(self.s(numbers=[-1, 0], target=-1), [1, 2])


if __name__ == "__main__":
    unittest.main()
