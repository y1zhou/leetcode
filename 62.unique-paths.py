#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
# https://leetcode.com/problems/unique-paths/
# Tagged "array" and "dynamic programming".
#
import unittest
from typing import List, Optional

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Calculate binom(m+n-2, n-1)
        total_steps = m + n - 2
        down_steps = n - 1

        ans = 1
        for i in range(1, n):
            ans = ans * (total_steps - down_steps + i) / i

        return int(ans)


# @lc code=end


class DpSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
        return ans[m - 1][n - 1]


class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        m, n = 3, 2
        self.assertEqual(Solution().uniquePaths(m, n), 3)

    def test_example2(self) -> None:
        m, n = 7, 3
        self.assertEqual(Solution().uniquePaths(m, n), 28)

    def test_single_grid(self) -> None:
        self.assertEqual(Solution().uniquePaths(1, 1), 1)


if __name__ == "__main__":
    unittest.main()
