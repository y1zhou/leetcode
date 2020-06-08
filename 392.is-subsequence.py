#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
# Tagged "binary-search", "dynamic-programming" and "greedy".

import unittest
from collections import defaultdict
from bisect import bisect_left

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        The greedy algorithm would start at the beginning of both strings.
        When there's a match, both pointers move to the next character; if
        there isn't a match, then the pointer in `t` move to the next character.
        After going through both strings, if `s` is a substring of `t` then the
        pointer in `s` should be at the end of `s`.

        We can't change the positions of the characters in `t`, so while we
        go through each character in `s` and find its index in `t` as `i`, the
        next character in `s` must have an index that's greater than `i`. If for
        each character in `s`, we know all its positions in `t`, then the problem
        becomes finding the first element that's larger than a certain number in
        a sorted array, which can be solved using a binary search.

        """
        if not s:
            return True
        if not t:
            return False
        pos = defaultdict(list)
        for i, c in enumerate(t):
            pos[c].append(i)

        # prev_char_pos is the minimum index the next character has to be at,
        # so if we found a new position p, then the updated prev_char_pos should
        # be p + 1.
        prev_char_pos = 0
        for c in s:
            if c not in pos:
                return False
            i = bisect_left(pos[c], prev_char_pos)
            if i == len(pos[c]):
                return False
            prev_char_pos = pos[c][i] + 1
        return True


# @lc code=end
class SolutionGreedy:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        si, ti = 0, 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                ti += 1
        return si == len(s)


class TestSolution(unittest.TestCase):
    def test_example(self):
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(Solution().isSubsequence(s, t))

    def test_not_substring(self):
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(Solution().isSubsequence(s, t))

    def test_extra_char(self):
        s = "abc"
        t = "bahbgdca"
        self.assertTrue(Solution().isSubsequence(s, t))


if __name__ == "__main__":
    unittest.main()
