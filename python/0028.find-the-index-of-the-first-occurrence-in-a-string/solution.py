# Created by Bob at 2024/02/23 17:06
# leetgo: 1.4.1
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(needle), len(haystack)
        for i in range(m - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1


# @lc code=end

if __name__ == "__main__":
    haystack: str = deserialize("str", read_line())
    needle: str = deserialize("str", read_line())
    ans = Solution().strStr(haystack, needle)
    print("\noutput:", serialize(ans, "integer"))
