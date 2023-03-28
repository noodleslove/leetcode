# Created by Bob at 2023/03/28 12:28
# https://leetcode.com/problems/reverse-string/

"""
344. Reverse String (Easy)
Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array
[in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.

**Example 1:**

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

```

**Example 2:**

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

```

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).
"""

# @lc code=begin

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

# @lc code=end
