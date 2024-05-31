# Created by Bob at 2024/05/29 11:37
# leetgo: 1.4.7
# https://leetcode.com/problems/range-sum-of-bst/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(root: Optional[TreeNode], total) -> int:
            if root is None:
                return total

            if root.val < low:
                return total + traverse(root.right, total)
            elif low <= root.val <= high:
                return (
                    total
                    + root.val
                    + traverse(root.left, total)
                    + traverse(root.right, total)
                )
            else:
                return total + traverse(root.left, total)

        return traverse(root, 0)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    ans = Solution().rangeSumBST(root, low, high)
    print("\noutput:", serialize(ans, "integer"))
