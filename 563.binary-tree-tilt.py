#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#
# https://leetcode.com/problems/binary-tree-tilt/description/
# Tagged "tree"; should also include "binary-tree" and "recursion".

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        Our final goal is to find the sum of all nodes' tilt.

        The simple cases are:
          - if a node has no children nodes, its tilt is 0.
          - if a node has no grandchildren nodes, its tilt is
              abs(left.val - right.val)

                                 4
                                / \
                               2   9
                              / \   \
                             3   5   7

        In the example above, nodes 3, 5, 7 all have tilt=0. Tilt of
        node 2 is |3-5|=2, and tilt(9)=|7-0|=7. For the root node, the
        tilt is |(2+3+5)-(9+7)|=6. So the total tilt is 2+7+6=15.

        We need a global variable to keep track of the sum of tilt values
        at each recursion call. The function should calculate the tilt of
        the current node, add the tilt to the global variable and return
        the sum of the values of the current node and its children nodes.
        """

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            self.tilt_sum += abs(l - r)

            return node.val + l + r

        self.tilt_sum = 0
        dfs(root)
        return self.tilt_sum


# @lc code=end
class TestSolution(unittest.TestCase):
    def test_example(self) -> None:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(Solution().findTilt(root), 1)

    def test_deeper_tree(self) -> None:
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(9)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().findTilt(root), 15)


if __name__ == "__main__":
    unittest.main()
