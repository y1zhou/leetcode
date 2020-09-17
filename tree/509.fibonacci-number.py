#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/
# Tagged "tree".
#
import unittest

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        """
        Avoid re-computing numbers. For each number in the sequence,
        we only need the sum of the previous two numbers.
        Using a tuple here is slightly faster than using a list.
        """
        if N == 0:
            return 0
        ans = (0, 1)
        for _ in range(2, N):
            ans = (ans[1], ans[0] + ans[1])
        return ans[0] + ans[1]


# @lc code=end
class SimpleRecursionSolution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        return self.fib(N - 2) + self.fib(N - 1)


class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        self.assertEqual(Solution().fib(2), 1)

    def test_example2(self) -> None:
        self.assertEqual(Solution().fib(3), 2)

    def test_zero(self) -> None:
        self.assertEqual(Solution().fib(0), 0)


if __name__ == "__main__":
    unittest.main()
