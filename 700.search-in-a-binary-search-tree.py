#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# Tagged "tree" (binary-tree).
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_example(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        res = Solution().searchBST(root, 2)
        self.assertEqual(res.val, 2)
        self.assertEqual(res.left.val, 1)
        self.assertEqual(res.right.val, 3)
        self.assertIsNone(res.left.left)
        self.assertIsNone(res.left.right)
        self.assertIsNone(res.right.left)
        self.assertIsNone(res.right.right)

    def test_empty(self):
        root = TreeNode(3, TreeNode(1), TreeNode(10))
        self.assertIsNone(Solution().searchBST(root, 0))


if __name__ == "__main__":
    unittest.main()
