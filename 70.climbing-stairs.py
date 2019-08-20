#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        x, y = 1, 2
        for i in range(3, n + 1):
            z = x + y
            x = y
            y = z
        return y
