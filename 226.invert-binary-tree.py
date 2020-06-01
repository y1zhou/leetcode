#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Tagged "tree".
#
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = (
                self.invertTree(root.right),
                self.invertTree(root.left),
            )

        return root


# @lc code=end
class TestSolution(unittest.TestCase):
    def test_example(self) -> None:
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        ans = Solution().invertTree(root)
        self.assertEqual(ans.val, 4)
        self.assertEqual(ans.left.val, 7)
        self.assertEqual(ans.right.val, 2)
        self.assertEqual(ans.left.left.val, 9)
        self.assertEqual(ans.left.right.val, 6)
        self.assertEqual(ans.right.left.val, 3)
        self.assertEqual(ans.right.right.val, 1)


if __name__ == "__main__":
    unittest.main()
