#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit2Letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(digit2Letter[digits[0]])

        leading = self.letterCombinations(digits[:-1])
        return [y + x for y in leading for x in digit2Letter[digits[-1]]]
