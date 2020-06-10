#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
# Tagged "array" and "binary-search".

import unittest
from typing import List

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Obviously a situation for binary search. Below is what bisect.bisect_left does.
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.nums = [1, 3, 5, 6]
        self.x = Solution()

    def test_target_in_array(self) -> None:
        target = 5
        self.assertEqual(self.x.searchInsert(self.nums, target), 2)

    def test_insert(self) -> None:
        target = 2
        self.assertEqual(self.x.searchInsert(self.nums, target), 1)

    def test_append(self) -> None:
        target = 7
        self.assertEqual(self.x.searchInsert(self.nums, target), 4)

    def test_append_left(self) -> None:
        target = 0
        self.assertEqual(self.x.searchInsert(self.nums, target), 0)


if __name__ == "__main__":
    unittest.main()
