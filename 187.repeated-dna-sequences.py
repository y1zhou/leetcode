#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# @lc code=start
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        if len(s) <= 10:
            return ans
        ans = defaultdict(lambda: 0)
        for i in range(0, len(s) - 9):
            ans[s[i : i + 10]] += 1

        return [seq for seq, n in ans.items() if n > 1]


# @lc code=end
