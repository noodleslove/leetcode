# Created by Eddie Ho at 2023/08/01 23:40
# leetgo: 1.3.3
# https://leetcode.com/problems/break-a-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
            
        return palindrome[:-1] + "b"

# @lc code=end

if __name__ == "__main__":
    palindrome: str = deserialize("str", read_line())
    ans = Solution().breakPalindrome(palindrome)

    print("\noutput:", serialize(ans))
