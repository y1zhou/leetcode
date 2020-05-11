#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

import unittest
from typing import List

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            return sum(nums)  # stop if n <= 3
        nums.sort()  # sort so that we know which direction to move to
        kmax = len(nums) - 1  # k starts from the back

        best_sum = nums[0] + nums[1] + nums[kmax]
        for i in range(kmax - 1):
            j, k = i + 1, kmax
            # Test two extreme cases; move i if target not in range
            if nums[i] + nums[j] + nums[j + 1] >= target:
                k = j + 1
            if nums[i] + nums[k - 1] + nums[k] <= target:
                j = k - 1
            while j < k:
                ans = nums[i] + nums[j] + nums[k]
                if ans == target:
                    return ans

                if abs(ans - target) < abs(best_sum - target):
                    best_sum = ans

                if ans < target:
                    j += 1
                else:
                    k -= 1
        return best_sum


class TestSolution(unittest.TestCase):
    def test_given(self):
        nums = [-1, 2, 1, -4]
        target = 1
        self.assertEqual(Solution().threeSumClosest(nums, target), 2)

    def test_short(self):
        nums = [1, 2]
        target = 100
        self.assertEqual(Solution().threeSumClosest(nums, target), 3)

    def test_negative(self):
        nums = [1, 1, 1, 0]
        target = -100
        self.assertEqual(Solution().threeSumClosest(nums, target), 2)


if __name__ == "__main__":
    unittest.main()
# @lc code=end
