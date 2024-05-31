# Created by Bob at 2024/05/29 18:19
# leetgo: 1.4.7
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_XOR = [0] + arr[:]
        n = len(prefix_XOR)

        for i in range(1, n):
            prefix_XOR[i] ^= prefix_XOR[i - 1]

        count = 0
        for start in range(n):
            for end in range(start + 1, n):
                if prefix_XOR[start] == prefix_XOR[end]:
                    count += end - start - 1

        return count


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countTriplets(arr)
    print("\noutput:", serialize(ans, "integer"))
