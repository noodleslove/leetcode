# Created by Eddie Ho at 2023/08/05 23:14
# leetgo: 1.3.6
# https://leetcode.com/problems/sum-of-subarray-ranges/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            min_val = float('inf')
            max_val = float('-inf')
            for j in range(i, len(nums)):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])

                ans += max_val - min_val
        return ans

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subArrayRanges(nums)

    print("\noutput:", serialize(ans))
