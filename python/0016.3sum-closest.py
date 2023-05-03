# Created by Bob at 2023/04/28 15:10
# https://leetcode.com/problems/3sum-closest/

"""
16. 3Sum Closest (Medium)
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums`
such that the sum is closest to `target`.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

**Example 1:**

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

```

**Example 2:**

```
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

```

**Constraints:**

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10⁴ <= target <= 10⁴`

"""

# @lc code=begin

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = output = float('inf')
        for i in range(n):
            start, end = i + 1, n - 1
            while start < end:
                curr = nums[i] + nums[start] + nums[end]
                if curr == target:
                    return curr
                elif curr < target:
                    start += 1
                else:
                    end -= 1
                if abs(curr - target) < closest:
                    closest = abs(curr - target)
                    output = curr
        return output

# @lc code=end
