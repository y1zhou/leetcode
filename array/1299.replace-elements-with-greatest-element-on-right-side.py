#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#
import unittest
from typing import List

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """Start from the back and replace elements with the observed maximum."""
        ans: List[int] = [-1] * len(arr)
        cur_max = arr[len(arr) - 1]

        for i in range(len(arr) - 2, -1, -1):
            ans[i] = cur_max
            cur_max = max(cur_max, arr[i])

        return ans


# @lc code=end
class TestSolution(unittest.TestCase):
    def test_example(self) -> None:
        arr = [17, 18, 5, 4, 6, 1]
        self.assertEqual(Solution().replaceElements(arr), [18, 6, 6, 6, 1, -1])

    def test_single_element(self) -> None:
        arr = [10]
        self.assertEqual(Solution().replaceElements(arr), [-1])


if __name__ == "__main__":
    unittest.main()
