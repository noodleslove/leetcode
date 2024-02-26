# Created by Bob at 2024/01/09 19:24
# leetgo: 1.4
# https://leetcode.com/problems/container-with-most-water/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = float("-inf")
        while l < r:
            water = min(height[l], height[r]) * (r - l)
            maxWater = max(maxWater, water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater


# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(height)

    print("\noutput:", serialize(ans))
