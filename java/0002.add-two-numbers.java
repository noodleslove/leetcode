// Created by Eddie Ho at 2023/11/12 23:41
// leetgo: 1.3.8
// https://leetcode.com/problems/add-two-numbers/

// @lc code=begin

import utils.ListNode;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode p1 = l1;
        ListNode p2 = l2;
        
        ListNode output = new ListNode();
        ListNode o1 = output;

        int carry = 0;

        while (p1 != null && p2 != null) {
            int num = (p1.val + p2.val + carry) % 10;
            carry = Math.floorDiv(p1.val + p2.val + carry, 10);

            o1.next = new ListNode(num);

            o1 = o1.next;
            p1 = p1.next;
            p2 = p2.next;
        }

        while (p1 != null) {
            int num = (p1.val + carry) % 10;
            carry = Math.floorDiv(p1.val + carry, 10);

            o1.next = new ListNode(num);

            o1 = o1.next;
            p1 = p1.next;
        }

        while (p2 != null) {
            int num = (p2.val + carry) % 10;
            carry = Math.floorDiv(p2.val + carry, 10);

            o1.next = new ListNode(num);

            o1 = o1.next;
            p2 = p2.next;
        }

        if (carry > 0) {
            o1.next = new ListNode(carry);
        }

        return output.next;
    }
}

// @lc code=end
