# Created by Eddie Ho at 2023/12/06 22:59
# leetgo: 1.3.8
# https://leetcode.com/problems/integer-to-roman/

from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]

        return (
            thousands[num // 1000]
            + hundreds[(num % 1000) // 100]
            + tens[(num % 100) // 10]
            + ones[num % 10]
        )


# @lc code=end


if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().intToRoman(num)

    print("\noutput:", serialize(ans))
