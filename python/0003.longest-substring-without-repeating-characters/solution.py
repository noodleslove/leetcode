# Created by Bob at 2024/02/27 00:53
# leetgo: 1.4.1
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        left, out = 0, 0

        for i in range(len(s)):
            letter = s[i]

            # update left pointer
            if letter in letters:
                left = max(left, letters[letter] + 1)

            letters[letter] = i
            out = max(out, i - left + 1)

        return out


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
