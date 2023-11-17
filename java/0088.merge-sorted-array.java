// Created by Eddie Ho at 2023/11/16 14:20
// leetgo: 1.3.8
// https://leetcode.com/problems/merge-sorted-array/

// @lc code=begin

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = m + n - 1, j = m - 1, k = n - 1; i >= 0; i--) {
            if (j >= 0 && k >= 0 && nums1[j] < nums2[k]) {
                nums1[i] = nums2[k];
                k--;
            } else if (j >= 0 && k >= 0) {
                nums1[i] = nums1[j];
                j--;
            } else if (j >= 0) {
                nums1[i] = nums1[j];
                j--;
            } else {
                nums1[i] = nums2[k];
                k--;
            }
        }
    }
}

// @lc code=end
