#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        if a[-1] == b[-1] == "1":
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), "1") + "0"
        elif a[-1] == b[-1] == "0":
            return self.addBinary(a[:-1], b[:-1]) + "0"
        else:
            return self.addBinary(a[:-1], b[:-1]) + "1"
