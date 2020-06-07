#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/
# Tagged "greedy".
#
import unittest
from typing import List

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        If we pick out the shortest person, the `k` would be the same as the number
        of people in front of this person. Note how this person doesn't affect the
        position of anyone else in the list.

        If we remove the shortest person, the second shortest person becomes the
        shortest, and doesn't affect the positions of other people anymore. Thus,
        when we're constructing the returned list, we should start from the tallest
        people first, because their positions are going to affect all the others.

        Now going to the example:
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

        The tallest people have h=7, so we start from
            [[7, 0], [7, 1]]
        The next person has h=6 and k=1, so should be inserted in the middle:
            [[7, 0], [6, 1], [7, 1]]
        After the next round, the list becomes
            [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]

        We can see that in each round, the person is inserted to the i-th position
        where `i` is equal to the person's `k`. If there's multiple people with
        the same height, then we first insert the person with a smaller `k`.
        """
        ans: List[List[int]] = []

        ppl_sorted = sorted(people, key=lambda x: (-x[0], x[1]))
        for person in ppl_sorted:
            ans.insert(person[1], person)
        return ans


# @lc code=end


class TestSolution(unittest.TestCase):
    def test_example(self):
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        ans = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        self.assertEqual(Solution().reconstructQueue(people), ans)


if __name__ == "__main__":
    unittest.main()
