# Created by Eddie Ho at 2023/08/04 15:10
# leetgo: 1.3.6
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def search(start, end):
            mid = (start + end) // 2

            if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
                return mid
            elif arr[mid-1] > arr[mid]:
                return search(start, mid)
            else:
                return search(mid + 1, end)
            
        return search(0, len(arr))

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().peakIndexInMountainArray(arr)

    print("\noutput:", serialize(ans))
