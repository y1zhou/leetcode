#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
# Tagged "array" and "backtracking".
# For backtracking, here's an excellent tutorial:
# https://www.geeksforgeeks.org/backtracking-algorithms/

import unittest
from typing import List

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        We don't use dynamic programming here because we want all possible results,
        not the best possible result or the number of results. A recursion (depth-first
        search) should be applied here.

        We loop through `candidates` and add the element to a list `tmp`. If the sum of
        the list becomes greater than `target`, then `tmp` is dropped; if the sum of
        `tmp` is exactly `target`, then we add it to our list of answers; if the sum of
        `tmp` is smaller than `target`, we continue adding the next number.

        If we follow the procedure above, clearly we'd want `candidates` to be sorted
        and without duplicates.
        """
        ans = []
        # sort array, but no need to remove duplicates in this problem
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)

        return ans

    def dfs(
        self,
        candidates: List[int],
        target: int,
        start: int,
        combination: List[int],
        ans: List[List[int]],
    ) -> None:
        # found answer
        if target == 0:
            ans.append(combination)
            return
        # backtracking
        if target < 0:
            return
        for i in range(start, len(candidates)):
            # we've sorted the array, so everything afterwards is larger than target
            if candidates[i] > target:
                break
            self.dfs(
                candidates,
                target - candidates[i],
                i,
                combination + [candidates[i]],
                ans,
            )


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_example1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        ans = [[7], [2, 2, 3]]
        self.assertCountEqual(Solution().combinationSum(candidates, target), ans)

    def test_example2(self):
        candidates = [2, 3, 5]
        target = 8
        ans = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertCountEqual(Solution().combinationSum(candidates, target), ans)


if __name__ == "__main__":
    unittest.main()
