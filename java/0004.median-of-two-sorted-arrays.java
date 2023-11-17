// Created by Eddie Ho at 2023/11/13 12:50
// leetgo: 1.3.8
// https://leetcode.com/problems/median-of-two-sorted-arrays/

// @lc code=begin

import java.util.Vector;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length, n2 = nums2.length;
        int n = n1 + n2;
        int p1 = 0, p2 = 0;
        Vector<Integer> combined = new Vector<>();

        while (p1 < n1 && p2 < n2) {
            if (nums1[p1] <= nums2[p2]) {
                combined.add(nums1[p1]);
                p1++;
            } else {
                combined.add(nums2[p2]);
                p2++;
            }
        }

        while (p1 < n1) {
            combined.add(nums1[p1]);
            p1++;
        }

        while (p2 < n2) {
            combined.add(nums2[p2]);
            p2++;
        }

        if (n % 2 == 0) {
            return (combined.get(n / 2) + combined.get(n / 2 - 1)) / 2.0;
        } else {
            return combined.get(n / 2);
        }
    }
}

// @lc code=end
