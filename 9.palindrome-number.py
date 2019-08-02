#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # The easy way:
        return str(x) == str(x)[::-1]

        # The hard way without converting int -> str:
        # if 0 <= x < 10:
        #     return True

        # if x < 0 or x % 10 == 0:
        #     return False

        # y = x
        # xnew = 0
        # while x != 0:
        #     xnew *= 10
        #     xnew += x % 10

        #     x //= 10

        # return y == xnew
