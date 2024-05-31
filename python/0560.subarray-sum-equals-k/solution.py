# Created by Bob at 2024/05/29 19:11
# leetgo: 1.4.7
# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] + nums[:]
        n = len(prefix_sum)
        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]
        count = 0
        sums = {}
        for i in range(n):
            if prefix_sum[i] - k in sums:
                count += sums[prefix_sum[i] - k]
            sums[prefix_sum[i]] = sums.get(prefix_sum[i], 0) + 1
        return count


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraySum(nums, k)
    print("\noutput:", serialize(ans, "integer"))
