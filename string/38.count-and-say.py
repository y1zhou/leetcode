#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        def saySeq(seq):
            i, digitCount = 0, 1
            ans = ""
            while i < len(seq):
                while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                    i += 1
                    digitCount += 1
                ans += str(digitCount) + seq[i]
                i += 1
                digitCount = 1
            return ans

        ans = "1"
        for i in range(n - 1):
            ans = saySeq(ans)

        return ans
