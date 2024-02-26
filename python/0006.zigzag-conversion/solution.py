# Created by Bob at 2024/02/23 21:55
# leetgo: 1.4.1
# https://leetcode.com/problems/zigzag-conversion/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        newS = [""] * numRows
        i, step = 0, 1
        for c in s:
            newS[i] += c
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step
        return "".join(newS)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    numRows: int = deserialize("int", read_line())
    ans = Solution().convert(s, numRows)
    print("\noutput:", serialize(ans, "string"))
