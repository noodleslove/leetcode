# Created by Bob at 2024/02/26 19:19
# leetgo: 1.4.1
# https://leetcode.com/problems/candy/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        out = [1] * n

        # check left side
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                out[i] = out[i - 1] + 1

        # check right side
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if i > 0 and ratings[i - 1] < ratings[i]:
                    out[i] = max(out[i - 1], out[i + 1]) + 1
                else:
                    out[i] = out[i + 1] + 1

        return sum(out)


# @lc code=end

if __name__ == "__main__":
    ratings: List[int] = deserialize("List[int]", read_line())
    ans = Solution().candy(ratings)
    print("\noutput:", serialize(ans, "integer"))
