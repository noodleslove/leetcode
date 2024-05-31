# Created by Bob at 2024/05/28 23:03
# leetgo: 1.4.7
# https://leetcode.com/problems/get-equal-substrings-within-budget/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]

        left = 0
        cost = 0
        maxLen = 0
        for right in range(len(s)):
            cost += costs[right]

            if cost <= maxCost:
                maxLen = max(maxLen, right - left + 1)

            while cost > maxCost:
                cost -= costs[left]
                left += 1

        return maxLen


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    maxCost: int = deserialize("int", read_line())
    ans = Solution().equalSubstring(s, t, maxCost)
    print("\noutput:", serialize(ans, "integer"))
