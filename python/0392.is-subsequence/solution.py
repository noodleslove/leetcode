# Created by Eddie Ho at 2023/11/21 14:36
# leetgo: 1.3.8
# https://leetcode.com/problems/is-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isSubsequence(s, t)

    print("\noutput:", serialize(ans))
