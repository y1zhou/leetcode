#
# @lc app=leetcode id=1416 lang=python3
#
# [1416] Restore The Array
# https://leetcode.com/problems/restore-the-array/
# Tagged "dynamic programming".
#
import unittest
from typing import List

# @lc code=start
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        All integers in the array are in the range [1, k] and there are no leading zeroes.
        Return the number of possible array that can be printed as a string s.
        The number of ways could be very large so return it modulo 10^9 + 7.

        Build an array dp where dp[i] is the number of ways you can divide the string
        starting from index i to the end.
        """
        ans = [0] * len(s) + [1]
        nums = [int(x) for x in s] + [k + 1]  # ensure the last num > k to break loop
        for i in range(len(s) - 1, -1, -1):
            num = nums[i]
            j = i + 1
            while 1 <= num <= k and j < len(nums):
                ans[i] = (ans[i] + ans[j]) % 1000000007
                num = 10 * num + nums[j]
                j += 1
        return ans[0]


# @lc code=end


class TopDownSolution:
    def __init__(self) -> None:
        self.ans: List[int] = []

    def numberOfArrays(self, s: str, k: int) -> int:
        self.ans = [0] * len(s) + [1]  # there's only one way to "split" the tail
        return self.dfs(s, k, 0)

    def dfs(self, s: str, k: int, i: int) -> int:
        # memoization
        if self.ans[i] != 0:
            return self.ans[i]

        if "0" == s[i]:
            return 0  # numbers can't start with 0

        for j in range(i + 1, len(s) + 1):
            num = int(s[i:j])
            if num > k:
                break
            self.ans[i] = (self.ans[i] + self.dfs(s, k, j)) % 1000000007
        return self.ans[i]


class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        s = "1000"
        k = 10000
        self.assertEqual(Solution().numberOfArrays(s, k), 1)

    def test_example2(self) -> None:
        s = "1000"
        k = 10
        self.assertEqual(Solution().numberOfArrays(s, k), 0)

    def test_example3(self) -> None:
        s = "1317"
        k = 2000
        self.assertEqual(Solution().numberOfArrays(s, k), 8)

    def test_example4(self) -> None:
        s = "2020"
        k = 30
        self.assertEqual(Solution().numberOfArrays(s, k), 1)

    def test_example5(self) -> None:
        s = "1234567890"
        k = 90
        self.assertEqual(Solution().numberOfArrays(s, k), 34)


if __name__ == "__main__":
    unittest.main()
