#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
# https://leetcode.com/problems/map-sum-pairs/
# This problem is about the trie data structure. Each node keeps track of the sum of its children.
# A new key overrides the original values.
#
import unittest
from typing import Dict

# @lc code=start
class Node:
    def __init__(self, val: int = 0):
        self.value = val
        self.children: Dict[str, Node] = {}


class MapSum:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.root_node = Node()
        self.keys: Dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        # override if key already exists
        val_diff = val - self.keys.get(key, 0)
        self.keys[key] = val

        # track count of prefix characters
        node = self.root_node
        for c in key:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.value += val_diff

    def sum(self, prefix: str) -> int:
        node = self.root_node
        for c in prefix:
            # return 0 if prefix doesn't exist
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# @lc code=end
class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        x = MapSum()
        x.insert("apple", 3)
        self.assertEqual(x.sum("ap"), 3)
        x.insert("app", 2)
        self.assertEqual(x.sum("ap"), 5)

    def test_override(self) -> None:
        x = MapSum()
        x.insert("apple", 3)
        x.insert("app", 2)
        x.insert("apple", 8)
        self.assertEqual(x.sum("ap"), 10)


if __name__ == "__main__":
    unittest.main()
