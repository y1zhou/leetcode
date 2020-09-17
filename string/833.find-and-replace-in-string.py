#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#
# https://leetcode.com/problems/find-and-replace-in-string/description/
# Tagged "string".

import unittest
from typing import List

# @lc code=start
class Solution:
    def findReplaceString(
        self, S: str, indexes: List[int], sources: List[str], targets: List[str]
    ) -> str:
        """
        Keep in mind when we change a substring, the indices downstream are going
        to be affected if the source and the target aren't of the same length.

        To avoid keeping track of the length of the string, we can go from the back
        of the string.
        """
        for i, source, target in sorted(zip(indexes, sources, targets), reverse=True):
            if source == S[i : i + len(source)]:
                S = S[:i] + target + S[i + len(source) :]
        return S


# @lc code=end


class SolutionForward:
    def findReplaceString(
        self, S: str, indexes: List[int], sources: List[str], targets: List[str]
    ) -> str:
        str_len_diff = 0
        for i, source, target in zip(indexes, sources, targets):
            i += str_len_diff
            if source == S[i : i + len(source)]:
                S = S[:i] + target + S[i + len(source) :]
                str_len_diff += len(target) - len(source)
        return S


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        S = "abcd"
        indexes = [0, 2]
        sources = ["a", "cd"]
        targets = ["eee", "ffff"]
        self.assertEqual(
            self.s.findReplaceString(S, indexes, sources, targets), "eeebffff"
        )

    def test_example2(self):
        S = "abcd"
        indexes = [0, 2]
        sources = ["ab", "ec"]
        targets = ["eee", "ffff"]
        self.assertEqual(
            self.s.findReplaceString(S, indexes, sources, targets), "eeecd"
        )


if __name__ == "__main__":
    unittest.main()
