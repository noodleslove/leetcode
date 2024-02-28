# Created by Bob at 2024/02/26 13:36
# leetgo: 1.4.1
# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float("inf")
        i, j, n = 0, 0, len(nums)
        while j < n:
            total = sum(nums[i:j])
            while total >= target:
                best = min(best, j - i)
                total -= nums[i]
                i += 1
            j += 1
        return 0 if best == float("inf") else best


# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSubArrayLen(target, nums)
    print("\noutput:", serialize(ans, "integer"))
