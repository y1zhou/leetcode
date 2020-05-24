#
# @lc app=leetcode id=1247 lang=python3
#
# [1247] Minimum Swaps to Make Strings Equal
# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
#
import unittest

# @lc code=start
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """s1 and s2 are of equal length and only contain letters 'x' and 'y'.
        There's two types of differences in s1 and s2:
          - x_y: s1[i] == 'x' and s2[i] == 'y',
          - y_x: s1[i] == 'y' and s2[i] == 'x'.
        2 differences of the same type require 1 swap;
        2 differences of different types require 2 swaps.
        """
        x_y, y_x = 0, 0
        for i, j in zip(s1, s2):
            if i != j:
                if i == "x":
                    x_y += 1
                else:
                    y_x += 1
        # it's impossible if the total number of differences is odd
        if (x_y + y_x) % 2 == 1:
            return -1

        # If one of x_y and y_x is an odd number, then the other must also be an odd number.
        # In this case we need 2 more swaps.
        return ((x_y + 1) // 2) + ((y_x + 1) // 2)


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_given1(self):
        s1, s2 = "xx", "yy"
        self.assertEqual(Solution().minimumSwap(s1, s2), 1)

    def test_given2(self):
        s1, s2 = "xy", "yx"
        self.assertEqual(Solution().minimumSwap(s1, s2), 2)

    def test_given3(self):
        s1, s2 = "xx", "xy"
        self.assertEqual(Solution().minimumSwap(s1, s2), -1)

    def test_given4(self):
        s1 = "xxyyxyxyxx"
        s2 = "xyyxyxxxyx"
        self.assertEqual(Solution().minimumSwap(s1, s2), 4)


if __name__ == "__main__":
    unittest.main()
