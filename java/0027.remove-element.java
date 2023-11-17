// Created by Eddie Ho at 2023/11/16 20:11
// leetgo: 1.3.8
// https://leetcode.com/problems/remove-element/

// @lc code=begin

class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0, right = nums.length - 1;
        int count = 0;
        while (left <= right) {
            if (nums[left] != val) {
                count++;
                left++;
            } else {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                right--;
            }
        }
        return count;
    }
}

// @lc code=end
