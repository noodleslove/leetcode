# Created by Bob at 2024/02/27 18:03
# leetgo: 1.4.1
# https://leetcode.com/problems/minimum-window-substring/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        left = 0
        counter = {k: -v for k, v in Counter(t).items()}
        minLength = float("inf")
        out = ""
        for right in range(len(s)):
            ch = s[right]
            if ch in counter:
                counter[ch] += 1
            while all(v >= 0 for v in counter.values()):
                if right + 1 - left < minLength:
                    out = s[left : right + 1]
                    minLength = right + 1 - left
                if s[left] in counter:
                    counter[s[left]] -= 1
                left += 1
        return out


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minWindow(s, t)
    print("\noutput:", serialize(ans, "string"))
