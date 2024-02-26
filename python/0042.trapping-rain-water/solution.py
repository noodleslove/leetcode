# Created by Eddie Ho at 2023/12/06 22:54
# leetgo: 1.3.8
# https://leetcode.com/problems/trapping-rain-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        ans = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    ans += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    ans += r_max - height[r]
                r -= 1

        return ans

# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trap(height)

    print("\noutput:", serialize(ans))
