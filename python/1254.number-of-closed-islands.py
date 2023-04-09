# Created by Bob at 2023/04/08 21:29
# https://leetcode.com/problems/number-of-closed-islands/

"""
1254. Number of Closed Islands (Medium)
Given a 2D `grid` consists of `0s` (land) and `1s` (water).  An island is a maximal 4-directionally
connected group of `0s` and a closed island is an island **totally** (all left, top, right, bottom)
surrounded by `1s.`

Return the number of closed islands.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png)

```
Input: grid =
[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png)

```
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

```

**Example 3:**

```
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

```

**Constraints:**

- `1 <= grid.length, grid[0].length <= 100`
- `0 <= grid[i][j] <=1`

"""

# @lc code=begin


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0 and self.dfs(grid, row, col):
                    count += 1
        return count

    def dfs(self, grid, row, col):
        n, m = len(grid), len(grid[0])

        if row < 0 or n <= row or col < 0 or m <= col:
            return False
        
        if grid[row][col] == 1:
            return True
        
        grid[row][col] = 1
        left = self.dfs(grid, row, col-1)
        right = self.dfs(grid, row, col+1)
        up = self.dfs(grid, row-1, col)
        down = self.dfs(grid, row+1, col)

        return left and right and up and down


# @lc code=end
