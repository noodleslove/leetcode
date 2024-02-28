# Created by Bob at 2024/02/27 17:19
# leetgo: 1.4.1
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def isPermutation(subString: str) -> bool:
            return (
                Counter([subString[i : i + m] for i in range(0, len(subString), m)])
                == counter
            )

        counter = Counter(words)
        n, m = len(words), len(words[0])
        out = []
        for i in range(len(s) - n * m + 1):
            if isPermutation(s[i : i + n * m]):
                out.append(i)
        return out


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findSubstring(s, words)
    print("\noutput:", serialize(ans, "integer[]"))
