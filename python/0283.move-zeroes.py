# Created by Bob at 2023/03/25 15:50
# https://leetcode.com/problems/move-zeroes/

"""
283. Move Zeroes (Easy)
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order
of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

**Example 1:**

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

**Example 2:**

```
Input: nums = [0]
Output: [0]

```

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `-2³¹ <= nums[i] <= 2³¹ - 1`

**Follow up:** Could you minimize the total number of operations done?
"""

# @lc code=begin

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        write_pt = 0

        # Move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[write_pt] = num
                write_pt += 1

        # Set all remaining elements to zero
        while write_pt < n:
            nums[write_pt] = 0
            write_pt += 1

# @lc code=end
