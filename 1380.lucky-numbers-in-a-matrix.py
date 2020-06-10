#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/

import unittest
from typing import List

# @lc code=start
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        We know all the elements in the m * n matrix are in [1, 10e5]. The lucky number
        is defined as an element s.t. it's the minimum in its row and maximum in its column.
        We can show that there can be at most one lucky number in a matrix of distinct
        numbers. Suppose `l` is a lucky number, then b < l < c. Then `a` cannot be
        another lucky number because c < a < b can't hold.

        | a  ...  b |
        |           |
        | c  ...  l |

        So we only need to find the minimum of all column maximums, and see if it coincides
        with the maximum of all row minimums.
        """
        max_of_row_minimums = max((min(col) for col in matrix))
        min_of_col_maximums = min((max(row) for row in zip(*matrix)))
        return (
            [max_of_row_minimums] if max_of_row_minimums == min_of_col_maximums else []
        )


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        mat = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
        self.assertEqual(self.s.luckyNumbers(mat), [15])

    def test_example2(self):
        mat = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
        self.assertEqual(self.s.luckyNumbers(mat), [12])

    def test_no_lucky_num(self):
        mat = [[3, 7, 8], [9, 11, 13], [17, 16, 10]]
        self.assertEqual(self.s.luckyNumbers(mat), [])


if __name__ == "__main__":
    unittest.main()
