# Created by Bob at 2024/05/28 23:49
# leetgo: 1.4.7
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, base=2)
        count = 0
        while num > 1:
            count += 1
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
        return count


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numSteps(s)
    print("\noutput:", serialize(ans, "integer"))
