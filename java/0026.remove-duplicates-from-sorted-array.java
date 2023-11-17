// Created by Eddie Ho at 2023/11/16 23:41
// leetgo: 1.3.8
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

// @lc code=begin

class Solution {
    public int removeDuplicates(int[] nums) {
        int slow = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[slow] = nums[i];
                slow++;
            }
        }
        return slow;
    }
}

// @lc code=end
