// Created by Eddie Ho at 2023/11/17 00:05
// leetgo: 1.3.8
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

// @lc code=begin

class Solution {
    public int removeDuplicates(int[] nums) {
        int slow = 1;
        for (int i = 1; i < nums.length; i++) {
            if ((slow < 2) || (nums[slow - 2] != nums[i])) {
                nums[slow] = nums[i];
                slow++;
            }
        }
        return slow;
    }
}

// @lc code=end
