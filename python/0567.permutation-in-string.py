# Created by Bob at 2023/04/10 23:36
# https://leetcode.com/problems/permutation-in-string/

"""
567. Permutation in String (Medium)
Given two strings `s1` and `s2`, return `true` if  `s2` contains a permutation of  `s1`, or  `false`
otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1:**

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

```

**Example 2:**

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

```

**Constraints:**

- `1 <= s1.length, s2.length <= 10⁴`
- `s1` and `s2` consist of lowercase English letters.

"""

# @lc code=begin
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        n = len(s1)

        for i, ch in enumerate(s2):
            if ch in s1_counter:
                s1_counter[ch] -= 1

            if i >= n and s2[i-n] in s1_counter:
                s1_counter[s2[i-n]] += 1

            if all(val == 0 for val in s1_counter.values()):
                return True
            
        return False

# @lc code=end
