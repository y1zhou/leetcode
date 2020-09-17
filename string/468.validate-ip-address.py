"""
We may assume there's no extra space or special characters in the input string.
Beware of negative signs!

# IPv4
- Check if there's four parts separated by dots.
- In each part,
  - there should be no characters other than "0"-"9";
  - the number should range from 0 to 255; and
  - there can't be leading zeros.


# IPv6
- Eight groups of four hexadecimal digits separated by colons.
- Case-insensitive.
- It's fine to omit leading zeros, but "0000" should become "0" and can't be empty.
- Extra leading zeros is also invalid.
"""
#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#
# https://leetcode.com/problems/validate-ip-address/
# Tagged "string".

import unittest

# @lc code=start
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s: str) -> bool:
            # four parts separated by dots
            if s.count(".") != 3:
                return False

            for num in s.split("."):
                # no other characters; just a positive number
                if not num.isnumeric():
                    return False
                # leading zeros
                if len(num) > 1 and num[0] == "0":
                    return False
                # out of range
                if int(num) > 255:
                    return False

            return True

        def isIPv6(s: str) -> bool:
            if s.count(":") != 7:
                return False
            for num in s.split(":"):
                # empty values or extra-long values
                if not num or len(num) > 4:
                    return False
                # valid hexadecimal characters
                if not all(c in "0123456789abcdefABCDEF" for c in num):
                    return False

            return True

        if isIPv4(IP):
            return "IPv4"
        if isIPv6(IP):
            return "IPv6"

        return "Neither"


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_valid_ipv4(self) -> None:
        self.assertEqual(self.s.validIPAddress("172.16.254.1"), "IPv4")

    def test_ipv4_character(self) -> None:
        self.assertEqual(self.s.validIPAddress("-172.16.254.1"), "Neither")
        self.assertEqual(self.s.validIPAddress("172.16.254.a1"), "Neither")

    def test_ipv4_wrong_num_parts(self) -> None:
        self.assertEqual(self.s.validIPAddress("192.168..0.1"), "Neither")
        self.assertEqual(self.s.validIPAddress("0.0.0"), "Neither")

    def test_ipv4_out_of_range(self) -> None:
        self.assertEqual(self.s.validIPAddress("256.256.256.256"), "Neither")

    def test_ipv4_leading_zero(self) -> None:
        self.assertEqual(self.s.validIPAddress("172.16.254.01"), "Neither")

    def test_valid_ipv6(self) -> None:
        self.assertEqual(
            self.s.validIPAddress("2001:0db8:85a3:0:00:8A2E:0370:7334"), "IPv6"
        )

    def test_ipv6_wrong_length(self) -> None:
        self.assertEqual(
            self.s.validIPAddress("02001:0db8:85a3:0:0:8A2E:0370:7334"), "Neither"
        )
        self.assertEqual(
            self.s.validIPAddress("0db8:85a3:0:0:8A2E:0370:7334"), "Neither"
        )

    def test_ipv6_other_chars(self) -> None:
        self.assertEqual(
            self.s.validIPAddress("020g:0db8:85a3:0:0:8A2E:0370:7334"), "Neither"
        )
        self.assertEqual(
            self.s.validIPAddress("-20:0db8:85a3:0:0:8A2E:0370:7334"), "Neither"
        )


if __name__ == "__main__":
    unittest.main()
