# Created by Bob at 2024/02/23 13:15
# leetgo: 1.4.1
# https://leetcode.com/problems/length-of-last-word/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().rsplit(maxsplit=1)[-1])


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLastWord(s)
    print("\noutput:", serialize(ans, "integer"))
