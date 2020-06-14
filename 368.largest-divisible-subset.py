#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/
# Tagged "math" and "dynamic-programming".
import unittest
from typing import List

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        This is a classic dynamic programming case. Our `dp` array would be the same
        length as `nums`, and `dp[i]` would store the length of the largest subset with `nums[i]` as the largest number.

        Traversing the array would be more efficient if we sort `nums` first, because we
        can always try to divide a number with numbers on its left.

        When we go to the next number (a larger one), it can only be appended to sequences
        that end with a factor of this new number. For example, 4 can be appended to [1, 2],
        but not to [1, 3] because 3 is not a factor of 4.

        So for any new number i, we just need to find the length of all the sequences before
        it that ends with its factor, and add set dp[i] as that length plus 1.

        To be able to re-construct the full subset, at each point in `dp` we also need to
        know the index of the previous number in the sequence.
        """
        n = len(nums)
        if n <= 1:
            return nums
        arr = sorted(nums)
        # initialize array to store the max length at each step, and the index of the
        # previous number
        dp = [1] * n
        prev_idx = [n] * n  # it's impossible for the previous index to be n

        # the maximum length should start from 1, because we can at least include 1 number
        max_idx = 0
        for i in range(1, n):
            for j in range(i):
                if arr[i] % arr[j] == 0 and dp[j] + 1 > dp[i]:
                    # if the new number can be appended, compare the current max length
                    # and the length of appending to dp[j]
                    dp[i] = dp[j] + 1
                    prev_idx[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i

        # re-construct the subset
        i, res = max_idx, []
        while i < n:  # when i == n we've hit the first element
            res.append(arr[i])
            i = prev_idx[i]

        return res


# @lc code=end
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_example1(self) -> None:
        nums = [1, 2, 3]
        self.assertIn(self.s.largestDivisibleSubset(nums), [[2, 1], [3, 1]])

    def test_example2(self) -> None:
        nums = [1, 2, 4, 8]
        self.assertEqual(self.s.largestDivisibleSubset(nums), [8, 4, 2, 1])

    def test_empty(self) -> None:
        self.assertEqual(self.s.largestDivisibleSubset([]), [])
        self.assertEqual(self.s.largestDivisibleSubset([10]), [10])

    def test_longer(self) -> None:
        nums = [1, 2, 4, 5, 6, 8, 9, 12, 16, 18]
        self.assertEqual(self.s.largestDivisibleSubset(nums), [16, 8, 4, 2, 1])

    def test_two_elements(self) -> None:
        nums = [546, 669]
        self.assertIn(self.s.largestDivisibleSubset(nums), [[546], [669]])

    def test_no_first_element(self) -> None:
        nums = [3, 4, 16, 8]
        self.assertEqual(self.s.largestDivisibleSubset(nums), [16, 8, 4])


if __name__ == "__main__":
    unittest.main()
