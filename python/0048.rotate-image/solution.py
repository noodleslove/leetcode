# Created by Bob at 2024/02/28 00:08
# leetgo: 1.4.1
# https://leetcode.com/problems/rotate-image/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top, right, left, bottom = [0, 0], [0, n - 1], [n - 1, 0], [n - 1, n - 1]

        for i in range(1, n):
            while top[1] < right[1]:
                (
                    matrix[top[0]][top[1]],
                    matrix[right[0]][right[1]],
                    matrix[left[0]][left[1]],
                    matrix[bottom[0]][bottom[1]],
                ) = (
                    matrix[left[0]][left[1]],
                    matrix[top[0]][top[1]],
                    matrix[bottom[0]][bottom[1]],
                    matrix[right[0]][right[1]],
                )
                top[1] += 1
                right[0] += 1
                left[0] -= 1
                bottom[1] -= 1
            top[0] += 1
            top[1] = i
            right[0] = i
            right[1] -= 1
            left[0] = n - i - 1
            left[1] += 1
            bottom[0] -= 1
            bottom[1] = n - i - 1


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    rotate(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))
