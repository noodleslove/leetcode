# Created by Eddie Ho at 2023/11/21 14:30
# leetgo: 1.3.8
# https://leetcode.com/problems/valid-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(str.isalnum, s.lower()))
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isPalindrome(s)

    print("\noutput:", serialize(ans))
