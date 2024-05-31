# Created by Bob at 2024/05/29 21:54
# leetgo: 1.4.7
# https://leetcode.com/problems/find-the-highest-altitude/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain) + 1
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + gain[i - 1]

        highest = 0
        for num in prefix:
            if num > highest:
                highest = num
        return highest


# @lc code=end

if __name__ == "__main__":
    gain: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestAltitude(gain)
    print("\noutput:", serialize(ans, "integer"))
