# Created by Eddie Ho at 2023/07/05 20:53
# leetgo: 1.3.3
# https://leetcode.com/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)

    print("\noutput:", serialize(ans))
