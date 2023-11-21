# Created by Eddie Ho at 2023/11/20 03:17
# leetgo: 1.3.8
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [float('inf')] * n

        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            for j in range(left + 1, right + 1):
                dp[j] = min(dp[j], dp[left] + 1)

        return dp[n] if dp[n] != float('inf') else -1

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ranges: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minTaps(n, ranges)

    print("\noutput:", serialize(ans))
