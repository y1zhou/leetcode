#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/
# Tests bit-manipulation.

import unittest
from typing import List

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ascii_a = ord("a")  # we only have lower-case letters
        masks: List[int] = [0] * len(words)

        for i, word in enumerate(words):
            for char in word:
                masks[i] |= 1 << (ord(char) - ascii_a)  # each bit represent a letter

        ans = 0
        for i, mask in enumerate(masks):
            for j in range(i + 1, len(masks)):
                if mask & masks[j] == 0:  # no cases of (1 & 1) at any position
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


# @lc code=end


class EasyUnderstandingSolution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set([char for char in word]) for word in words]
        ans = 0
        for i, word_set in enumerate(word_sets):
            for j in range(i + 1, len(word_sets)):
                if not word_set.intersection(word_sets[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
        # abcw and xtfn
        self.assertEqual(Solution().maxProduct(words), 16)

    def test_example2(self) -> None:
        words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
        # ab and cd
        self.assertEqual(Solution().maxProduct(words), 4)

    def test_example3(self) -> None:
        words = ["a", "aa", "aaa", "aaaa"]
        # no such pair of words
        self.assertEqual(Solution().maxProduct(words), 0)


if __name__ == "__main__":
    unittest.main()
