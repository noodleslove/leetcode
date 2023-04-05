# Created by Bob at 2023/04/03 19:52
# https://leetcode.com/problems/merge-intervals/

"""
56. Merge Intervals (Medium)
Given an array of `intervals` where `intervals[i] = [startᵢ, endᵢ]`, merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the intervals in the
input.

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

```

**Constraints:**

- `1 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= startᵢ <= endᵢ <= 10⁴`
"""

# @lc code=begin

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        i = 1
        output = []
        while i < n:
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                output.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

            i += 1
        else:
            output.append([start, end])

        return output

# @lc code=end
