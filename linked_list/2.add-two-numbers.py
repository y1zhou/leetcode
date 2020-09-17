#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        n = ans

        digit = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                digit += l1.val
                l1 = l1.next
            if l2 is not None:
                digit += l2.val
                l2 = l2.next

            n.next = ListNode(digit % 10)
            n = n.next
            digit //= 10  # start from 1 if previous sum >= 10
        if digit == 1:
            n.next = ListNode(1)
        return ans.next


# @lc code=end
