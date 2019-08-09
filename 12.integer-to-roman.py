#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        integers = [1000, 900, 500, 100, 90, 50, 10, 9, 5, 1]
        romans = ["M", "CM", "D", "C", "XC", "L", "X", "IX", "V", "I"]

        for i, digit in enumerate(integers):
            numDigit = num // digit
            if numDigit != 4:
                ans += romans[i] * numDigit
                num -= numDigit * digit
            else:
                ans += romans[i] + romans[i - 1]
                num -= 4 * digit
        return ans


if __name__ == "__main__":
    print(Solution().intToRoman(1994))  # "MMMCMXCIX"
