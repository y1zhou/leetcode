#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
# https://leetcode.com/problems/ugly-number/
# Tagged "math".
#
import unittest

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num > 0:
            prime_fcts = [5, 3, 2]
            for fct in prime_fcts:
                while num % fct == 0:
                    num //= fct

        return 1 == num


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        # 2 x 3 = 6
        self.assertTrue(Solution().isUgly(6))

    def test_example2(self) -> None:
        # 2 x 2 x 2 = 8
        self.assertTrue(Solution().isUgly(8))

    def test_example3(self) -> None:
        # 14 includes another prime factor 7
        self.assertFalse(Solution().isUgly(14))

    def test_non_positive(self) -> None:
        self.assertFalse(Solution().isUgly(0))
        self.assertFalse(Solution().isUgly(-2))
        self.assertFalse(Solution().isUgly(-7))


if __name__ == "__main__":
    unittest.main()
