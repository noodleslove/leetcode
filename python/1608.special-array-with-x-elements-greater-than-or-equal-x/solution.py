# Created by Bob at 2024/05/27 01:01
# leetgo: 1.4.7
# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and i == nums[i] else i


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().specialArray(nums)
    print("\noutput:", serialize(ans, "integer"))
