#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/
# Tagged "array".
import unittest
from typing import List

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        We're required to modify the matrix in-place. An idea is to take
        the transpose, then flip each row horizontally. This is the same
        as flipping each column vertically and then taking the transpose.
        """
        # flip each column
        matrix.reverse()
        N = len(matrix)
        # transpose
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # if we didn't flip the columns first
        # matrix[:] = [x[::-1] for x in matrix]


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_example_odd(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Solution().rotate(mat)
        ans = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(mat, ans)

    def test_example_even(self):
        mat = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        Solution().rotate(mat)
        ans = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        self.assertEqual(mat, ans)


if __name__ == "__main__":
    unittest.main()
