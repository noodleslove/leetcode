# Created by Bob at 2024/01/09 19:15
# leetgo: 1.4
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1

# @lc code=end

if __name__ == "__main__":
    numbers: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(numbers, target)

    print("\noutput:", serialize(ans))
