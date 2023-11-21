# Created by Eddie Ho at 2023/11/21 11:54
# leetgo: 1.3.8
# https://leetcode.com/problems/gas-station/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        idx = 0
        tank = 0

        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                idx = i + 1
                tank = 0

        return idx

# @lc code=end


if __name__ == "__main__":
    gas: List[int] = deserialize("List[int]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canCompleteCircuit(gas, cost)

    print("\noutput:", serialize(ans))
