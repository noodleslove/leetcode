# Created by Eddie Ho at 2023/11/19 18:59
# leetgo: 1.3.8
# https://leetcode.com/problems/product-of-array-except-self/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        prefix = suffix = 1

        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().productExceptSelf(nums)

    print("\noutput:", serialize(ans))
