#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/
#

import unittest

from typing import List

# @lc code=start
from random import randint, randrange


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_len = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # mimic what random.sample() does
        ans = [None] * self.nums_len
        picked = set()
        for i in range(self.nums_len):
            j = randint(0, self.nums_len - 1)
            while j in picked:
                j = randint(0, self.nums_len - 1)
            picked.add(j)
            ans[i] = self.nums[j]
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end


class FisherYatesAlgorithm:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx = randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


class TestSolution(unittest.TestCase):
    def test_given(self):
        nums = [1, 2, 3]
        x = Solution(nums)

        self.assertEqual(x.reset(), [1, 2, 3])
        self.assertIn(
            x.shuffle(),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )
        self.assertEqual(x.reset(), [1, 2, 3])

    def test_fisher_yates(self):
        nums = [1, 2, 3]
        x = FisherYatesAlgorithm(nums)

        self.assertEqual(x.reset(), [1, 2, 3])
        self.assertIn(
            x.shuffle(),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )
        self.assertEqual(x.reset(), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
