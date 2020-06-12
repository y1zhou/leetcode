#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
# Tagged "array" and "two-pointers".

import unittest
from collections import Counter
from typing import List

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        We first iterate through the array and count the elements using a dict.
        Then to find the answer there's two scenarios:
        (1) k=0, we only need to find numbers that appear more than once.
        (2) k>0, because (i, j) and (j, i) count as the same pair, we can loop through
        the dict and see (for i) if i+k is in the dict keys. In other words, we always
        look for the smaller number first to avoid counting the same pair twice.
        """
        if k < 0:
            return 0

        res = Counter(nums)

        if k == 0:
            return len([k for (k, v) in res.items() if v > 1])
        else:
            ans = 0
            for num in res:
                if num + k in res:  # k = |num1 - num2|
                    ans += 1
            return ans


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_dup_values(self):
        nums = [3, 1, 4, 1, 5]
        k = 2
        self.assertEqual(self.s.findPairs(nums, k), 2)

    def test_example(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        self.assertEqual(self.s.findPairs(nums, k), 4)

    def test_same_pair(self):
        nums = [1, 1, 3, 1, 3]
        k = 0
        self.assertEqual(self.s.findPairs(nums, k), 2)


if __name__ == "__main__":
    unittest.main()
