# Created by Bob at 2024/02/26 11:24
# leetgo: 1.4.1
# https://leetcode.com/problems/3sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            # skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[j] + nums[k] + nums[i]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    output.append([nums[j], nums[k], nums[i]])
                    # skip duplicate j
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # skip duplicate k
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

        return output


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeSum(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
