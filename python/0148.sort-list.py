# Created by Bob at 2023/03/25 17:06
# https://leetcode.com/problems/sort-list/

"""
148. Sort List (Medium)
Given the `head` of a linked list, return the list after sorting it in **ascending order**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)

```
Input: head = [4,2,1,3]
Output: [1,2,3,4]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)

```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

```

**Example 3:**

```
Input: head = []
Output: []

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 5 * 10⁴]`.
- `-10⁵ <= Node.val <= 10⁵`

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant
space)?
"""

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        L, R = self.split(head)

        # Recursive step
        L = self.sortList(L)
        R = self.sortList(R)

        return self.merge(L, R)
    
    def split(self, head):
        # Split list into half
        prev = None
        slow = head
        fast = head
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Cut the connection in the middle
        prev.next = None

        return head, slow
    
    def merge(self, L, R):
        left_pt = L
        right_pt = R
        
        output_pt = ListNode()
        prev = output_pt

        # Merge two lists
        while left_pt and right_pt:
            if left_pt.val < right_pt.val:
                prev.next = ListNode(left_pt.val)
                left_pt = left_pt.next
            else:
                prev.next = ListNode(right_pt.val)
                right_pt = right_pt.next
            prev = prev.next

        while left_pt:
            prev.next = ListNode(left_pt.val)
            prev = prev.next
            left_pt = left_pt.next

        while right_pt:
            prev.next = ListNode(right_pt.val)
            prev = prev.next
            right_pt = right_pt.next

        return output_pt.next

# @lc code=end
