# Created by Bob at 2023/03/29 18:12
# https://leetcode.com/problems/valid-parenthesis-string/

"""
678. Valid Parenthesis String (Medium)
Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return
`true`if `s`is **valid**.

The following rules define a **valid** string:

- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or
an empty string `""`.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "(*)"
Output: true

```

**Example 3:**

```
Input: s = "(*))"
Output: true

```

**Constraints:**

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.
"""

# @lc code=begin

class Solution:
    def checkValidString(self, s: str) -> bool:
        stars_min = stars_max = 0

        for c in s:
            if c == '(':
                stars_min += 1
                stars_max += 1
            elif c == ')':
                stars_min = max(stars_min-1, 0)
                stars_max -= 1
            else:
                stars_min = max(stars_min-1, 0)
                stars_max += 1

            if stars_max < 0:
                return False

        return stars_min == 0

# @lc code=end
