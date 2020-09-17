#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Tagged "linked-list".
#
import unittest
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        x = self.next
        res = [self.val]
        while x:
            res.append(x.val)
            x = x.next
        return " -> ".join([str(ele) for ele in res])


# @lc code=start
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Maintain a pointer (prev) to the node previous to the duplicated nodes (node).
        Once we reach the last duplicate node, we can make prev.next = node.next and
        update node=node.next. This would delete the nodes with duplicated values.
        We need another pointer (ans) at the very beginning to return the complete result.
        """
        if head is None or head.next is None:
            return head

        # ans.next is going to be the returned head node
        ans = ListNode(head.val - 1)  # ensure the value is different from the head's
        ans.next = head

        prev = ans
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                # NOTE: the following line *will* change ans as well
                prev.next = head.next  # head is still pointing to the last dup value
            else:
                # NOTE: the following line *won't* change ans; it will change the node
                # prev is pointing to in ans, so that the unique nodes will remain
                prev = prev.next
            head = head.next

        return ans.next


# @lc code=end
def ConstructLinkedList(nums: List[int]) -> ListNode:
    tail = ListNode(nums[len(nums) - 1])
    for i in range(len(nums) - 2, -1, -1):
        node = ListNode(nums[i])
        node.next = tail
        tail = node
    return tail


class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        given_list = ConstructLinkedList([1, 2, 3, 3, 4, 4, 5])
        return_list = ConstructLinkedList([1, 2, 5])
        ans = Solution().deleteDuplicates(given_list)
        while ans:
            self.assertEqual(ans.val, return_list.val)
            ans = ans.next
            return_list = return_list.next

    def test_example2(self) -> None:
        given_list = ConstructLinkedList([1, 1, 1, 2, 3])
        return_list = ConstructLinkedList([2, 3])
        ans = Solution().deleteDuplicates(given_list)
        while ans:
            self.assertEqual(ans.val, return_list.val)
            ans = ans.next
            return_list = return_list.next

    def test_single_element(self) -> None:
        given_list = ListNode(1)
        ans = Solution().deleteDuplicates(given_list)
        self.assertEqual(ans.val, 1)
        self.assertIsNone(ans.next)

    def test_none(self) -> None:
        given_list = ConstructLinkedList([1, 1, 2, 2])
        self.assertIsNone(Solution().deleteDuplicates(given_list))


if __name__ == "__main__":
    unittest.main()
