# Created by Bob at 2023/03/25 00:26
# https://leetcode.com/problems/squares-of-a-sorted-array/

"""
977. Squares of a Sorted Array (Easy)
Given an integer array `nums` sorted in **non-decreasing** order, return an array of **the squares
of each number** sorted in non-decreasing order.

**Example 1:**

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```

**Example 2:**

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

```

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`
- `nums` is sorted in **non-decreasing** order.

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an
`O(n)` solution using a different approach?
"""

# @lc code=begin

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Pointers on "nums"
        left = 0
        right = n - 1
        
        # Pointer on output list
        write_pt = n - 1

        # Initialize output list
        squares = n * [0]

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                squares[write_pt] = left_square
                left += 1
            else:
                squares[write_pt] = right_square
                right -= 1

            write_pt -= 1

        return squares

# @lc code=end
