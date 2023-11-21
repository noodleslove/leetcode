# Created by Eddie Ho at 2023/11/19 12:20
# leetgo: 1.3.8
# https://leetcode.com/problems/unique-paths-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    continue
                elif i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1]

        return dp[n - 1][m - 1]

# @lc code=end

if __name__ == "__main__":
    obstacleGrid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().uniquePathsWithObstacles(obstacleGrid)

    print("\noutput:", serialize(ans))
