#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
class Solution:
    def isHappy(self, n: int) -> bool:
        def happyNum(x):
            ans = 0
            while x > 0:
                tmp = x % 10
                ans += tmp * tmp
                x //= 10
            return ans

        res = set()
        while n not in res:
            res.add(n)
            n = happyNum(n)
            if n == 1:
                return True
        return False
