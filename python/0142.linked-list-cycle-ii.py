# Created by Bob at 2023/03/26 12:47
# https://leetcode.com/problems/linked-list-cycle-ii/

"""
142. Linked List Cycle II (Medium)
Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle,
return  `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node
that tail's `next` pointer is connected to ( **0-indexed**). It is `-1` if there is no cycle. **Note
that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 10⁴]`.
- `-10⁵ <= Node.val <= 10⁵`
- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?
"""

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # tortoise and hair algorithm
        while fast and fast.next:
            # increment pointers
            slow = slow.next
            fast = fast.next.next

            # stop loop when two pointers meet
            if slow == fast:
                break
        else:
            return None
            
        # increment til head and slow pinters meet
        while head != slow:
            head = head.next
            slow = slow.next
        
        return head

# @lc code=end
