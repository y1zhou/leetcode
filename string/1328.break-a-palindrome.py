#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#
import unittest

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return f"{palindrome[:i]}a{palindrome[i+1:]}"
        return f"{palindrome[:-1]}b"  # only happens for all 'a's


# @lc code=end
class TestSolution(unittest.TestCase):
    def test_given(self):
        self.assertEqual(Solution().breakPalindrome("abccba"), "aaccba")

    def test_odd_number(self):
        self.assertEqual(Solution().breakPalindrome("abcba"), "aacba")

    def test_single_letter(self):
        self.assertEqual(Solution().breakPalindrome("a"), "")

    def test_all_a(self):
        self.assertEqual(Solution().breakPalindrome("aaaa"), "aaab")


if __name__ == "__main__":
    unittest.main()
