# Created by Bob at 2024/05/30 22:52
# leetgo: 1.4.7
# https://leetcode.com/problems/single-number-iii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def checkBit(self, num: int, i: int) -> bool:
        return num & (1 << i) != 0

    def bitPos(self, num: int) -> int:
        for i in range(32):
            if self.checkBit(num, i):
                return i

    def singleNumber(self, nums: List[int]) -> List[int]:
        x, n = 0, len(nums)
        if n == 2:
            return nums

        for i in range(n):
            x ^= nums[i]

        pos = self.bitPos(x)
        x1, x2 = 0, 0
        for i in range(n):
            if self.checkBit(nums[i], pos):
                x1 ^= nums[i]
            else:
                x2 ^= nums[i]

        return [x1, x2]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)
    print("\noutput:", serialize(ans, "integer[]"))
