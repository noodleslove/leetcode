# Created by Bob at 2023/04/05 17:53
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
3. Longest Substring Without Repeating Characters (Medium)
Given a string `s`, find the length of the **longest** **substring** without repeating characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

**Constraints:**

- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols and spaces.
"""

# @lc code=begin


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = maximum = 0
        last_seen = {}

        for i, ch in enumerate(s):
            if ch in last_seen:
                left = max(left, last_seen[ch]+1)

            maximum = max(maximum, i-left+1)
            last_seen[ch] = i

        return maximum


# @lc code=end
