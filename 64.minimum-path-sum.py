#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
# Tagged "array" and "dynamic programming".
#
import unittest
from typing import List

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        The minimum sum to get to point (i, j) is:
          min(sum[i-1, j], sum[i, j-1])
        because we can only move right or down. In this case we also have to
        treat the first row and column differently, because there's no points
        above the first row, and similarly none to the left of the first column.

        The easiest way would be to maintain a matrix that's the same size as
        `grid` (SolutionFullTable), and return the final value in the bottom-right cell.

        But we don't have to maintain the entire table! for filling values in
        the (i, j) cell, we only need the j-th and the (j-1)-th columns to calculate
        all the values we need (SolutionTwoColumns).

        A further inspection of SolutionTwoColumns shows that c1 is just a copy of c2
        after each iteration, so we only need to modify c2 in-place.
        """
        m, n = len(grid), len(grid[0])

        col = [grid[0][0]] * m

        # initialize the first column
        for i in range(1, m):
            col[i] = col[i - 1] + grid[i][0]

        # modify the column in-place for the other columns
        for j in range(1, n):
            # first row is calculated separately
            col[0] = col[0] + grid[0][j]

            # now we have the previous column stored in `col`, and col[0] is
            # modified to be the first row of the current column, so we can
            # find the rest of the column accordingly
            for i in range(1, m):
                col[i] = min(col[i - 1], col[i]) + grid[i][j]

        return col[m - 1]


# @lc code=end


class SolutionFullTable:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = [[0 for _ in range(n)] for _ in range(m)]
        ans[0][0] = grid[0][0]
        # first row
        for j in range(1, n):
            ans[0][j] = ans[0][j - 1] + grid[0][j]
        # first column
        for i in range(1, m):
            ans[i][0] = ans[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + grid[i][j]
        return ans[m - 1][n - 1]


class SolutionTwoColumns:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        c1 = [grid[0][0]] * m
        c2 = [0] * m

        # initialize the first column
        for i in range(1, m):
            c1[i] = c1[i - 1] + grid[i][0]

        # starting from the second column, we need both c1 and grid to find the values
        for j in range(1, n):
            # first row is calculated separately
            c2[0] = c1[0] + grid[0][j]

            # calculate the other values in the column
            for i in range(1, m):
                c2[i] = min(c2[i - 1], c1[i]) + grid[i][j]

            c1 = c2

        return c2[m - 1]


class TestSolution(unittest.TestCase):
    def test_example(self):
        # 1 -> 3 -> 1 -> 1 -> 1
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        self.assertEqual(Solution().minPathSum(grid), 7)


if __name__ == "__main__":
    unittest.main()
