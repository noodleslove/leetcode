# Created by Eddie Ho at 2023/08/04 15:21
# leetgo: 1.3.6
# https://leetcode.com/problems/missing-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        curr = 0
        for num in nums:
            if num > curr:
                return curr
        
            curr += 1

        return curr

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().missingNumber(nums)

    print("\noutput:", serialize(ans))
