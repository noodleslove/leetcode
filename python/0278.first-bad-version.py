# Created by Bob at 2023/03/24 15:32
# https://leetcode.com/problems/first-bad-version/

"""
278. First Bad Version (Easy)
You are a product manager and currently leading a team to develop a new product. Unfortunately, the
latest version of your product fails the quality check. Since each version is developed based on the
previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which
causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement
a function to find the first bad version. You should minimize the number of calls to the API.

**Example 1:**

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

```

**Example 2:**

```
Input: n = 1, bad = 1
Output: 1

```

**Constraints:**

- `1 <= bad <= n <= 2³¹ - 1`
"""

# @lc code=begin

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n+1

        # Binary search
        while left < right:
            mid = (right + left) // 2
            is_mid_bad = isBadVersion(mid)
            
            # Check "mid" is the first version or its previous version is good
            is_mid_left_good = mid == 1 or not isBadVersion(mid-1)

            if is_mid_bad and is_mid_left_good:
                return mid
            elif not is_mid_bad:
                left = mid + 1
            else:
                right = mid

        # No bad version was found
        return n

# @lc code=end
