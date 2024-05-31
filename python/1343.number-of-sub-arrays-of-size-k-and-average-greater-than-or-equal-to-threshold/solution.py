# Created by Bob at 2024/05/29 19:36
# leetgo: 1.4.7
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr) + 1
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i - 1]

        res = 0
        for right in range(k, n):
            if prefix[right] - prefix[right - k] >= threshold * k:
                res += 1

        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().numOfSubarrays(arr, k, threshold)
    print("\noutput:", serialize(ans, "integer"))
