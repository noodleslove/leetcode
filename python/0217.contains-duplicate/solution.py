# Created by Eddie Ho at 2023/08/04 12:25
# leetgo: 1.3.6
# https://leetcode.com/problems/contains-duplicate/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1

        return False

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().containsDuplicate(nums)

    print("\noutput:", serialize(ans))
