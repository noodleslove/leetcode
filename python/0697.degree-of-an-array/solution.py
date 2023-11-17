# Created by Eddie Ho at 2023/08/02 00:37
# leetgo: 1.3.6
# https://leetcode.com/problems/degree-of-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, count, degree = {}, {}, 0
        ans = 0

        for i, num in enumerate(nums):
            first.setdefault(num, i)
            count[num] = count.get(num, 0) + 1

            if count[num] > degree:
                degree = count[num]
                ans = i - first[num] + 1
            elif count[num] == degree:
                ans = min(ans, i - first[num] + 1)

        return ans

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findShortestSubArray(nums)

    print("\noutput:", serialize(ans))
