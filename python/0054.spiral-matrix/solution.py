# Created by Bob at 2024/02/28 23:09
# leetgo: 1.4.1
# https://leetcode.com/problems/spiral-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIdx = 0
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        out = []
        for _ in range(m * n):
            out.append(matrix[i][j])
            seen.add((i, j))
            d = dirs[dirIdx]
            if (
                i + d[0] >= m
                or j + d[1] >= n
                or j + d[1] < 0
                or (i + d[0], j + d[1]) in seen
            ):
                dirIdx = (dirIdx + 1) % 4
                d = dirs[dirIdx]
            i += d[0]
            j += d[1]
        return out


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().spiralOrder(matrix)
    print("\noutput:", serialize(ans, "integer[]"))
