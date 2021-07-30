#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (53.66%)
# Likes:    1589
# Dislikes: 231
# Total Accepted:    396.2K
# Total Submissions: 738.1K
# Testcase Example:  '3'
#
# Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
# Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
#
#
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
#
# Constraints:
#
#
# 0 <= rowIndex <= 33
#
#
#
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
# space?
#
#
import unittest
from typing import List


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        1 3 3 1

        0 1 3 3 1
        1 3 3 1 0
        ---------
        1 4 6 4 1
        """
        res = [1]
        for _ in range(rowIndex):
            res = [x + y for x, y in zip([0] + res, res + [0])]

        return res


# @lc code=end


class SlowSolution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        res = [1] * (rowIndex + 1)
        prevRow = self.getRow(rowIndex - 1)
        for i in range(1, rowIndex):
            res[i] = prevRow[i - 1] + prevRow[i]

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().getRow

    def test_example1(self):
        self.assertEqual(self.s(3), [1, 3, 3, 1])

    def test_example2(self):
        self.assertEqual(self.s(0), [1])

    def test_example3(self):
        self.assertEqual(self.s(1), [1, 1])


if __name__ == "__main__":
    unittest.main()
