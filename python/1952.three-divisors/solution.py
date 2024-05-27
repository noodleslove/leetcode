# Created by Bob at 2024/05/12 12:05
# leetgo: 1.4.7
# https://leetcode.com/problems/three-divisors/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isThree(self, n: int) -> bool:
        return sum(1 for i in range(1, n + 1) if n % i == 0) == 3


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isThree(n)
    print("\noutput:", serialize(ans, "boolean"))
