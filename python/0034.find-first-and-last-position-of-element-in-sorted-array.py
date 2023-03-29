# Created by Bob at 2023/03/28 12:14
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
34. Find First and Last Position of Element in Sorted Array (Medium)
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending
position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

```

**Example 3:**

```
Input: nums = [], target = 0
Output: [-1,-1]

```

**Constraints:**

- `0 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`
- `nums` is a non-decreasing array.
- `-10⁹ <= target <= 10⁹`
"""

# @lc code=begin

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first, last = mid, mid
                while first > -1 and nums[first] == target:
                    first -= 1
                while last < len(nums) and nums[last] == target:
                    last += 1
                return [first+1, last-1]
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return [-1, -1]

# @lc code=end
