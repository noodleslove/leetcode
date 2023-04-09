# Created by Bob at 2023/04/08 20:56
# https://leetcode.com/problems/minimum-size-subarray-sum/

"""
209. Minimum Size Subarray Sum (Medium)
Given an array of positive integers `nums` and a positive integer `target`, return the **minimal
length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray,
return `0` instead.

**Example 1:**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

**Example 2:**

```
Input: target = 4, nums = [1,4,4]
Output: 1

```

**Example 3:**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```

**Constraints:**

- `1 <= target <= 10⁹`
- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁴`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the
time complexity is `O(n log(n))`.

"""

# @lc code=begin

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minimum = float('inf')
        total = left = 0

        for right in range(n):
            total += nums[right]

            # reduce window when `total` >= `target`
            while total >= target:
                minimum = min(minimum, right-left+1)
                total -= nums[left]
                left += 1
        
        return 0 if isinstance(minimum, float) else minimum

# @lc code=end
