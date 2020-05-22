#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
import unittest
from typing import List

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # first find the XOR of the two numbers
        xor = 0
        for num in nums:
            xor ^= num

        # find a bit_i where one of the numbers is 1 and the other is 0
        bit_i = xor & -xor

        # find numbers that have bit_i as 1, and numbers with bit_i = 0
        # all the paired numbers will cancel out with XOR
        x, y = 0, 0
        for num in nums:
            if num & bit_i:
                x ^= num
            else:
                y ^= num
        return [x, y]


# @lc code=end


class AnotherSolution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for num in nums:
            if num in ans:
                ans.remove(num)
            else:
                ans.add(num)
        return list(ans)


class TestSolution(unittest.TestCase):
    def test_given(self):
        nums = [1, 2, 1, 3, 2, 5]
        self.assertEqual(Solution().singleNumber(nums), [3, 5])

    def test_other_solution(self):
        nums = [1, 2, 1, 3, 2, 5]
        self.assertEqual(AnotherSolution().singleNumber(nums), [3, 5])


if __name__ == "__main__":
    unittest.main()
