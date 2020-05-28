#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Tagged "hash-table" and "sort".
#
import unittest
import collections
from typing import Dict

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans: Dict[str, int] = collections.defaultdict(lambda: 0)
        for char in s:
            ans[char] += 1

        for char in t:
            if char not in ans:
                return False
            ans[char] -= 1
            if ans[char] == 0:
                del ans[char]

        return not ans


# @lc code=end
class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        self.assertTrue(Solution().isAnagram("anagram", "nagaram"))

    def test_example2(self) -> None:
        self.assertFalse(Solution().isAnagram("rat", "car"))

    def test_different_nums_of_characters(self) -> None:
        self.assertFalse(Solution().isAnagram("inputs", "puutins"))

    def test_unicode_true(self) -> None:
        self.assertTrue(Solution().isAnagram("测试", "试测"))

    def test_unicode_false(self) -> None:
        self.assertFalse(Solution().isAnagram("测试", "实测"))


if __name__ == "__main__":
    unittest.main()
