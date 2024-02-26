# Created by Bob at 2024/02/23 13:22
# leetgo: 1.4.1
# https://leetcode.com/problems/reverse-words-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)
        for i in range(n // 2):
            words[i], words[n - i - 1] = words[n - i - 1], words[i]
        return " ".join(words)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().reverseWords(s)
    print("\noutput:", serialize(ans, "string"))
