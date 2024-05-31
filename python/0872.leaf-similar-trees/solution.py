# Created by Bob at 2024/05/29 16:17
# leetgo: 1.4.7
# https://leetcode.com/problems/leaf-similar-trees/

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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafs(root: Optional[TreeNode], leaves: List[int]):
            if root.left is None and root.right is None:
                leaves.append(root.val)
                return

            if root.left:
                leafs(root.left, leaves)
            if root.right:
                leafs(root.right, leaves)

        leaves1 = []
        leaves2 = []

        leafs(root1, leaves1)
        leafs(root2, leaves2)

        return leaves1 == leaves2


# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().leafSimilar(root1, root2)
    print("\noutput:", serialize(ans, "boolean"))
