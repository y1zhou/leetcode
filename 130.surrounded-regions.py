"""
Given an `m x n` board, all the `O`'s that are not on the boarder and aren't connected
to an `O` on the boarder will be flipped to `X`.

We don't need to check anything if n or m <= 2, because nothing can be surrounded.
For larger boards, we need to find all `O`'s that are on the boarder or connected
to the boarder, and mark them with another character `I`; then we flip all the
remaining `O`'s to `X`, and change all the `I`s back to `O`.

X O X X    ->    X I X X    ->    X I X X    ->    X O X X
X O X X    ->    X I X X    ->    X I X X    ->    X O X X
X X O X    ->    X X O X    ->    X X X X    ->    X X X X
X O X X    ->    X I X X    ->    X I X X    ->    X O X X
"""
#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/
# Tagged "depth-first-search" (DFS), "breadth-first-search" (BFS) and "union-find".

import unittest
from queue import deque
from typing import List

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        if n < 3 or m < 3:
            return

        check_cells = deque()
        # first add all the O's on the border
        for i in range(m):
            if board[i][0] == "O":
                check_cells.append((i, 0))
            if board[i][n - 1] == "O":
                check_cells.append((i, n - 1))
        for j in range(1, n - 1):
            if board[0][j] == "O":
                check_cells.append((0, j))
            if board[m - 1][j] == "O":
                check_cells.append((m - 1, j))

        # change the border-connected O's to I
        while check_cells:
            i, j = check_cells.popleft()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "I"
                check_cells.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "I":
                    board[i][j] = "O"


# @lc code=end
class TestSolution(unittest.TestCase):
    def test_example(self) -> None:
        board_before = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        board_after = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        Solution().solve(board_before)
        self.assertEqual(board_before, board_after)

    def test_connected(self) -> None:
        board_before = [
            ["X", "O", "X", "X"],
            ["X", "O", "X", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        board_after = [
            ["X", "O", "X", "X"],
            ["X", "O", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        Solution().solve(board_before)
        self.assertEqual(board_before, board_after)


if __name__ == "__main__":
    unittest.main()
