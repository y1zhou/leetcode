#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
# https://leetcode.com/problems/house-robber-iii/
# This problem is tagged tree and depth-first-search.
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right


# @lc code=start
from typing import Tuple


class Solution:
    def rob_or_skip(self, root: TreeNode) -> Tuple[int, int]:
        """
        First element in returned tuple is the maximum possible money we get for robbing the
        root node, and second element is the maximum money for skipping the root node.
        If we rob the root node then the children nodes can't be robbed.
        If we skip the root node, then we may or may not rob the children nodes, so the second
        element should be the sum of the maximums of the children tuples.

            6                   (6+4+10, 2+1+2 + 3+10)
           / \                    /           \
          2   3         =>     (2+1+2, 4)   (3+10, 10)
           \   \                  \             \
            4   1               (4, 1+2)       (1, 10)
           / \   \                /   \           \
          1   2   10          (1, 0)  (2, 0)     (10, 0)
        """
        if root is None:
            return (0, 0)
        first = self.rob_or_skip(root.left)
        second = self.rob_or_skip(root.right)
        rob_root = root.val + first[1] + second[1]  # can't rob children nodes
        skip_root = max(first) + max(second)

        return (rob_root, skip_root)

    def rob(self, root: TreeNode) -> int:
        return max(self.rob_or_skip(root))


# @lc code=end


class SlowSolution:
    def rob(self, root: TreeNode) -> int:
        """
        We can't rob two directly-linked houses, so if we robbed the root node, then the children nodes
        cannot be robbed, but the grandchildren nodes can; if we didn't rob the root node, then we start
        from the children nodes and jump over the grandchildren nodes.
        """
        if root is None:
            return 0
        rob_root = root.val

        if root.left is not None:
            rob_root += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right is not None:
            rob_root += self.rob(root.right.left) + self.rob(root.right.right)

        rob_children = self.rob(root.left) + self.rob(root.right)

        return max(rob_root, rob_children)


class TestExample1(unittest.TestCase):
    def setUp(self) -> None:
        self.root = TreeNode(3)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.right = TreeNode(3)
        self.root.right.right = TreeNode(1)

    def testSolution(self) -> None:
        self.assertEqual(Solution().rob(self.root), 7)

    def testSlowSolution(self) -> None:
        self.assertEqual(SlowSolution().rob(self.root), 7)


class TestExample2(unittest.TestCase):
    def setUp(self) -> None:
        self.root = TreeNode(6)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.right = TreeNode(4)
        self.root.right.right = TreeNode(1)
        self.root.left.right.left = TreeNode(1)
        self.root.left.right.right = TreeNode(2)
        self.root.right.right.right = TreeNode(10)

    def testSolution(self) -> None:
        self.assertEqual(Solution().rob(self.root), 20)

    def testSlowSolution(self) -> None:
        self.assertEqual(SlowSolution().rob(self.root), 20)


if __name__ == "__main__":
    unittest.main()
