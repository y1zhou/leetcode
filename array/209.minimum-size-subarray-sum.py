#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

import unittest
from typing import List

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        sum_of_subarr = 0
        min_size = len(nums) + 1
        i, j = 0, 0
        while j < len(nums):
            sum_of_subarr += nums[j]
            j += 1
            while sum_of_subarr >= s:
                min_size = min(min_size, j - i)  # no +1 because we already had j++
                if min_size == 1:
                    return 1
                sum_of_subarr -= nums[i]
                i += 1

        if min_size == len(nums) + 1:
            return 0
        else:
            return min_size


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_given(self):
        nums = [2, 3, 1, 2, 4, 3]
        s = 7
        self.assertEqual(Solution().minSubArrayLen(s, nums), 2)

    def test_num_larger_than_s(self):
        nums = [2, 3, 1, 7, 1, 5]
        s = 6
        self.assertEqual(Solution().minSubArrayLen(s, nums), 1)


if __name__ == "__main__":
    unittest.main()
