#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Tagged "array" and "dynamic programming".

import unittest
from typing import List

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        The minimum cost of reaching step i is min(cost[i-1], cost[i-2]) plus
        the cost of i cost[i].
        """
        # Start from the third step since we can start from 0 or 1
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]

        # We can get to the top from the last or second-to-last step
        return min(cost[-1], cost[-2])


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        cost = [10, 15, 20]
        self.assertEqual(Solution().minCostClimbingStairs(cost), 15)

    def test_example2(self) -> None:
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.assertEqual(Solution().minCostClimbingStairs(cost), 6)


if __name__ == "__main__":
    unittest.main()
