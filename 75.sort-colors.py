#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
# Tagged "array", "two-pointers" and "sort".

import unittest
from typing import List

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        There's only three colors, so a two-pass counting sort is the most straightforward.
        The one-pass solution is called the Dutch national flag problem. We maintain three
        pointers: `red`, `white` and `blue` for integers 0, 1 and 2. We should have:
          - 0 in [0, red);
          - 1 in [red, white);
          - elements in [white, blue) are not sorted; and
          - 2 in [blue, n].
        """
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:  # include white=blue so we don't miss the last comparison
            if nums[white] == 0:
                nums[red], nums[white] = 0, nums[red]
                red += 1
                white += 1
            elif nums[white] == 2:
                nums[blue], nums[white] = 2, nums[blue]
                blue -= 1
            else:
                white += 1


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_example(self) -> None:
        nums = [2, 0, 2, 1, 1, 0]
        Solution().sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_similar_example(self) -> None:
        nums = [2, 1, 2, 0, 2, 0]
        Solution().sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
