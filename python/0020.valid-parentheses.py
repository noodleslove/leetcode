# Created by Bob at 2023/03/29 18:20
# https://leetcode.com/problems/valid-parentheses/

"""
20. Valid Parentheses (Easy)
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`,
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "()[]{}"
Output: true

```

**Example 3:**

```
Input: s = "(]"
Output: false

```

**Constraints:**

- `1 <= s.length <= 10⁴`
- `s` consists of parentheses only `'()[]{}'`.
"""

# @lc code=begin


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif len(stack) > 0 and ((ch == ')' and stack[-1] == '(')
                                     or (ch == '}' and stack[-1] == '{')
                                     or (ch == ']' and stack[-1] == '[')):
                stack.pop()
            else:
                return False

        return len(stack) == 0


# @lc code=end
