# Created by Bob at 2024/05/30 22:49
# leetgo: 1.4.7
# https://leetcode.com/problems/single-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)
    print("\noutput:", serialize(ans, "integer"))
