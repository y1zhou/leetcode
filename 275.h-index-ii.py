"""
By definition of h-index, we're looking for the first index in the sorted
array that satisfies

    citations[i] >= length(citations) - i

where `i` is the 0-based index in the citations array. `length(citations) - i`
is the number of papers that have at least `citations[i]` citations.

Since the array is sorted, we can use binary search to reduce the time complexity.
"""
#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/
# Tagged "binary-search".
import unittest
from typing import List

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        num_papers = len(citations)
        lo, hi = 0, num_papers - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            # citations[mid] papers have at least citations[mid] citations
            # this is the paper that defines the h-index
            if citations[mid] == num_papers - mid:
                return num_papers - mid

            # citations[mid] papers have more than citations[mid] citations
            # so we search in the left side
            elif citations[mid] > num_papers - mid:
                hi = mid - 1

            # otherwise we search in the right side
            else:
                lo = mid + 1

        return num_papers - hi - 1


# @lc code=end
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution().hIndex

    def test_example(self):
        citations = [0, 1, 3, 5, 6]
        #       h = [5, 4, 3, 2, 1]
        self.assertEqual(self.s(citations), 3)

    def test_ties(self):
        citations = [0, 2, 3, 3, 7, 9, 15, 23, 76]
        #       h = [9, 8, 7, 6, 5, 4, 3,  2,  1 ]
        self.assertEqual(self.s(citations), 5)


if __name__ == "__main__":
    unittest.main()
