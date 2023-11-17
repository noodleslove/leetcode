# Created by Eddie Ho at 2023/08/02 13:29
# leetgo: 1.3.6
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = {}
        ans = 0

        # populate count dict
        for idx, val in enumerate(time):
            val = val % 60
            remaining = (60 - val) % 60
            ans += count.get(remaining, 0)
            
            if val in count:
                count[val] += 1
            else:
                count[val] = 1

# @lc code=end

if __name__ == "__main__":
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numPairsDivisibleBy60(time)

    print("\noutput:", serialize(ans))
