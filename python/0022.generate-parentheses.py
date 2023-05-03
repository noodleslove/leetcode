# Created by Bob at 2023/04/19 17:37
# https://leetcode.com/problems/generate-parentheses/

"""
22. Generate Parentheses (Medium)
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed
parentheses.

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

**Example 2:**

```
Input: n = 1
Output: ["()"]

```

**Constraints:**

- `1 <= n <= 8`

"""

# @lc code=begin

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, 0, 0, '', res)
        return res

    def helper(self, n: int, left: int, right: int, s: str, res: List[str]) -> None:
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            self.helper(n, left + 1, right, s + '(', res)
        if right < left:
            self.helper(n, left, right + 1, s + ')', res)

# @lc code=end
