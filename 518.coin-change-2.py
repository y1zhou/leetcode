#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
# https://leetcode.com/problems/coin-change-2/
# Not tagged, but is a "knapsack" problem, therefore also a "dynamic-programming" problem.
#
import unittest
from typing import List

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        For each coin, in each step there's two options: we choose it or
        don't choose it. If we choose the coin, then our sub-problem 1 becomes
        finding the number of combinations with all the coins to get `amount-coin`.
        If we choose not to use the coin, then the sub-problem 2 becomes getting to
        `amount` with all the other coins.

        To build the `dp` matrix, let `dp[i][j]` be the number of combinations to
        get amount `j` using the first `i` coins. Now sub-problem 1 can be found as
        `dp[i][j-coins[i-1]]`. Here the `coins[i-1]` is the value of the i-th coin
        because `dp` has length `len(coins)+1`. If `j` is smaller than `coins[i-1]`,
        then we skip this step. Sub-problem 2 can be found as `dp[i-1][j]`.
        Sum up the two and we get `dp[i][j]`.

        We can do a bit better memory-wise. When updating `dp[i][j]`, we only need
        `dp[i-1][j]` and possibly `dp[i][j-coins[i-1]]`, which means we can just
        modify the first row in-place, therefore a one-dimensional array is enough.
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(1, amount + 1):
                if j >= coin:
                    dp[j] += dp[j - coin]

        return dp[amount]


# @lc code=end
class SolutionMoreMemory:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            # there's always one way of getting amount 0: choosing no coins
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = (
                    dp[i - 1][j] + dp[i][j - coins[i - 1]]
                    if j >= coins[i - 1]
                    else dp[i - 1][j]
                )

        return dp[-1][-1]


class TestSolution(unittest.TestCase):
    def test_example(self):
        amount = 5
        coins = [1, 2, 5]
        self.assertEqual(Solution().change(amount, coins), 4)

    def test_zero(self):
        amount = 3
        coins = [2]
        self.assertEqual(Solution().change(amount, coins), 0)

    def test_single_coin(self):
        amount = 10
        coins = [10]
        self.assertEqual(Solution().change(amount, coins), 1)


if __name__ == "__main__":
    unittest.main()
