#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (58.04%)
# Likes:    3134
# Dislikes: 148
# Total Accepted:    545.4K
# Total Submissions: 939.4K
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
#
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= numRows <= 30
#
#
#
import unittest
from typing import List


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  # numRows = 1
        if numRows > 1:
            res.append([1, 1])  # 2
        for i in range(3, numRows + 1):
            rowi = [1] * i
            for j in range(1, i - 1):
                rowi[j] = res[i - 2][j - 1] + res[i - 2][j]
            res.append(rowi)
        return res


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().generate

    def test_example1(self):
        self.assertEqual(
            self.s(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        )

    def test_example2(self):
        self.assertEqual(self.s(1), [[1]])


if __name__ == "__main__":
    unittest.main()
