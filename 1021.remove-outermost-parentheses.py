#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        ans = ""
        for x in S:
            if stack and not (len(stack) == 1 and ")" == x):
                ans += x
            if "(" == x:
                stack.append(x)
            else:
                stack.pop()

        return ans
