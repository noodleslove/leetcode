# Created by Bob at 2024/05/29 21:23
# leetgo: 1.4.7
# https://leetcode.com/problems/subarray-sums-divisible-by-k/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        prefix = [0] * n

        for i in range(1, n):
            prefix[i] = (nums[i - 1] + prefix[i - 1]) % k

        print(prefix)
        count = 0
        sums = {}
        for num in prefix[1:]:
            if num % k in sums:
                count += sums[num % k]
            if num in sums:
                count += sums[num]
            if num % k == 0:
                count += 1
            sums[num] = sums.get(num, 0) + 1
        return count


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraysDivByK(nums, k)
    print("\noutput:", serialize(ans, "integer"))
