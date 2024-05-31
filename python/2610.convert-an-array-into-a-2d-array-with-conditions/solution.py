# Created by Bob at 2024/05/29 16:30
# leetgo: 1.4.7
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while True:
            seen = set()
            curr = []
            for i in range(len(nums)):
                if nums[i] is not None and nums[i] not in seen:
                    seen.add(nums[i])
                    curr.append(nums[i])
                    nums[i] = None

            if curr:
                res.append(curr)
            else:
                break
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMatrix(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
