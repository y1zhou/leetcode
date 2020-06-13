#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
# Tagged "array", "hash-table" and "design".
import unittest
from random import randint
from typing import Dict, List


# @lc code=start
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums: List[int] = []
        self.loc: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.loc:
            return False
        self.loc[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.loc:
            return False
        i = self.loc.get(val)
        # We don't want removing this number to affect the index of all other numbers,
        # so we swap it with the last element in self.nums

        # can't use last_ele = self.nums.pop() directly in case it's the only element
        last_ele = self.nums[-1]
        self.nums[i] = last_ele  # put the last element to the indexed position
        self.loc[last_ele] = i  # and update it's position
        self.nums.pop()
        self.loc.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[randint(0, len(self.nums) - 1)]


# @lc code=end


class TestRandomizedSet(unittest.TestCase):
    def test_example(self) -> None:
        random_set = RandomizedSet()
        random_set.insert(1)
        self.assertFalse(random_set.remove(2))
        random_set.insert(2)
        self.assertIn(random_set.getRandom(), (1, 2))
        random_set.remove(1)
        self.assertFalse(random_set.insert(2))
        self.assertEqual(random_set.getRandom(), 2)

    def test_deleting_only_element(self) -> None:
        random_set = RandomizedSet()
        random_set.insert(1)
        self.assertTrue(random_set.remove(1))


if __name__ == "__main__":
    unittest.main()
