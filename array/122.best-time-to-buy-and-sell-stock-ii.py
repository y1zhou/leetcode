#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (59.59%)
# Likes:    4879
# Dislikes: 2119
# Total Accepted:    894.2K
# Total Submissions: 1.5M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
# 3.
#
#
# Example 2:
#
#
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are engaging multiple transactions at the same time. You must sell before
# buying again.
#
#
# Example 3:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e., max profit = 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4
#
#
#
import unittest
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Buying and selling on the same day doesn't affect the results.
        We can simply look for all increasing adjacent pairs in the array.
        """
        total_profit = 0

        for i in range(1, len(prices)):
            cur_sell = prices[i] - prices[i - 1]
            if cur_sell > 0:
                total_profit += cur_sell

        return total_profit


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().maxProfit

    def test_example1(self):
        self.assertEqual(self.s([7, 1, 5, 3, 6, 4]), 7)

    def test_example2(self):
        self.assertEqual(self.s([1, 2, 3, 4, 5]), 4)


def test_example3(self):
    self.assertEqual(self.s([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
