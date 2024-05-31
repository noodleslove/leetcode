# Created by Bob at 2024/05/29 10:34
# leetgo: 1.4.7
# https://leetcode.com/problems/assign-cookies/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        sIdx = 0
        gIdx = 0

        while gIdx < len(g) and sIdx < len(s):
            if g[gIdx] <= s[sIdx]:
                gIdx += 1
            sIdx += 1

        return gIdx


# @lc code=end

if __name__ == "__main__":
    g: List[int] = deserialize("List[int]", read_line())
    s: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findContentChildren(g, s)
    print("\noutput:", serialize(ans, "integer"))
