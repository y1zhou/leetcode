#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack_open = []

        for x in s:
            if x in "([{":
                stack_open.append(x)
            elif len(stack_open) == 0:
                return False
            elif (
                (")" == x and stack_open[-1] == "(")
                or ("]" == x and stack_open[-1] == "[")
                or ("}" == x and stack_open[-1] == "{")
            ):
                stack_open.pop()
            else:
                return False

        if len(stack_open) != 0:
            return False

        return True
