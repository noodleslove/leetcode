# Created by Bob at 2023/05/03 10:35
# https://leetcode.com/problems/multiply-strings/

"""
43. Multiply Strings (Medium)
Given two non-negative integers `num1` and `num2` represented as strings, return the product of
`num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"

```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"

```

**Constraints:**

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

"""

# @lc code=begin

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        output = ""
        for i in range(min(n, m)):
            product = int(num1[i]) * int(num2[i])
            digit = product % 10
            carry = product // 10

# @lc code=end
