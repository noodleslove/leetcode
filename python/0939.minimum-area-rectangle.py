# Created by Bob at 2023/04/17 18:37
# https://leetcode.com/problems/minimum-area-rectangle/

"""
939. Minimum Area Rectangle (Medium)
You are given an array of points in the **X-Y** plane `points` where `points[i] = [xᵢ, yᵢ]`.

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y
axes. If there is not any such rectangle, return `0`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

```

**Constraints:**

- `1 <= points.length <= 500`
- `points[i].length == 2`
- `0 <= xᵢ, yᵢ <= 4 * 10⁴`
- All the given points are **unique**.

"""

# @lc code=begin


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        min_area = float('inf')

        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))
            seen.add((x1, y1))

        return min_area if min_area < float('inf') else 0

# @lc code=end
