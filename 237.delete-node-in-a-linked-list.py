#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Tagged "linked list".


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


# @lc code=start


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        `node` is a pointer to the node to be deleted. We can't just use
        `node = node.next` because it's only going to change where the pointer
        points to, but leave the original linked list unchanged.
        """
        node.val = node.next.val
        node.next = node.next.next


# @lc code=end
