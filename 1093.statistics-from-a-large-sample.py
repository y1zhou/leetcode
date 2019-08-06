#
# @lc app=leetcode id=1093 lang=python3
#
# [1093] Statistics from a Large Sample
#

from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        imin, imax, imode, smean, smedian = -1, 0, 0, 0, 0
        sampleSize = 0
        for i in range(len(count)):
            if imin == -1 and count[i] != 0:
                imin = i
            if count[i] != 0:
                imax = i
            smean += i * count[i]
            sampleSize += count[i]
            if count[i] > count[imode]:
                imode = i

        if sampleSize % 2 == 0:
            midPoint = sampleSize // 2
            curPos = 0
            for i in range(imin, imax + 1):
                smedian += count[i]
                if curPos > 0:
                    smedian = (i + curPos) / 2
                    break
                if smedian > midPoint:
                    smedian = i
                    break
                elif smedian == midPoint:
                    curPos = i

        else:
            midPoint = sampleSize // 2 + 1
            for i in range(imin, imax + 1):
                smedian += count[i]
                if smedian > midPoint:
                    smedian = i
                    break

        return [
            float(imin),
            float(imax),
            smean / sampleSize,
            float(smedian),
            float(imode),
        ]

