# Created by Bob at 2024/02/27 21:42
# leetgo: 1.4.1
# https://leetcode.com/problems/valid-sudoku/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIDE = 9
        STEP = 3

        for i in range(SIDE):
            seen = set()
            for j in range(SIDE):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for i in range(SIDE):
            seen = set()
            for j in range(SIDE):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for i in range(0, SIDE, STEP):
            for j in range(0, SIDE, STEP):
                seen = set()
                for k in range(STEP):
                    for l in range(STEP):
                        if board[i + k][j + l] == ".":
                            continue
                        elif board[i + k][j + l] in seen:
                            return False
                        seen.add(board[i + k][j + l])

        return True


# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().isValidSudoku(board)
    print("\noutput:", serialize(ans, "boolean"))
