#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        tree_row = [root]
        while tree_row:
            ans.append(max(node.val for node in tree_row))
            tree_row = [
                child
                for node in tree_row
                for child in (node.left, node.right)
                if child is not None
            ]  # BFS

        return ans


# @lc code=end
