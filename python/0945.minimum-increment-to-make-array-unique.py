# Created by Bob at 2023/03/28 21:43
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

"""
945. Minimum Increment to Make Array Unique (Medium)
You are given an integer array `nums`. In one move, you can pick an index `i` where `0 <= i <
nums.length` and increment `nums[i]` by `1`.

Return the minimum number of moves to make every value in  `nums`**unique**.

The test cases are generated so that the answer fits in a 32-bit integer.

**Example 1:**

```
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

```

**Example 2:**

```
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

```

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `0 <= nums[i] <= 10⁵`
"""

# @lc code=begin


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        seen = set()
        ans, maximum = 0, nums[0]

        for num in nums:
            # when num already exist once
            if num in seen:
                maximum += 1  # new number would be current maximum + 1
                ans += maximum - num  # calculate diff, add to answer
                seen.add(maximum)  # add new number to set
            else:
                seen.add(num)  # add number to set
                maximum = max(maximum, num)  # update current maximum

        return ans


# @lc code=end
