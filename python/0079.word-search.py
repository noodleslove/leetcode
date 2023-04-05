# Created by Bob at 2023/04/03 20:44
# https://leetcode.com/problems/word-search/

"""
79. Word Search (Medium)
Given an `m x n` grid of characters `board` and a string `word`, return `true`if `word`exists in the
grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

```

**Constraints:**

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?
"""

# @lc code=begin

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        for row in range(n):
            for col in range(m):
                if (board[row][col] == word[0]
                    and self.bfs(board, row, col, word, 0)):
                        return True
        return False

    def bfs(self, board, row, col, word, ptr):
        n, m = len(board), len(board[0])
        if ptr == len(word):
            return True
        if (row < 0
            or n <= row
            or col < 0
            or m <= col
            or board[row][col] != word[ptr]):
            return False
        
        temp = board[row][col]
        board[row][col] = ' '
        found = (self.bfs(board, row-1, col, word, ptr+1)
                 or self.bfs(board, row+1, col, word, ptr+1)
                 or self.bfs(board, row, col-1, word, ptr+1)
                 or self.bfs(board, row, col+1, word, ptr+1))
        board[row][col] = temp
        return found
            

# @lc code=end
