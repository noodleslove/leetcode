# Created by Bob at 2024/02/23 13:26
# leetgo: 1.4.1
# https://leetcode.com/problems/longest-common-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPrefix(a: str, b: str) -> str:
            n = min(len(a), len(b))
            j = 0
            for i in range(n):
                if a[i] != b[i]:
                    break
                j += 1
            return a[:j]

        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = commonPrefix(prefix, strs[i])
        return prefix


# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestCommonPrefix(strs)
    print("\noutput:", serialize(ans, "string"))
