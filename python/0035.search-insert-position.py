# Created by Bob at 2023/03/24 16:01
# https://leetcode.com/problems/search-insert-position/

"""
35. Search Insert Position (Easy)
Given a sorted array of distinct integers and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2

```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1

```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4

```

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10⁴ <= target <= 10⁴`
"""

# @lc code=begin

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left

# @lc code=end
