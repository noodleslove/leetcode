# Created by Bob at 2024/05/29 10:49
# leetgo: 1.4.7
# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        for v in Counter(arr).values():
            if v in seen:
                return False
            else:
                seen.add(v)
        return True


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().uniqueOccurrences(arr)
    print("\noutput:", serialize(ans, "boolean"))
