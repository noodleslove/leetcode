// Created by Eddie Ho at 2023/11/17 17:14
// leetgo: 1.3.8
// https://leetcode.com/problems/jump-game/

// @lc code=begin

class Solution {
    public boolean canJump(int[] nums) {
        int reachable = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reachable) { return false; }
            reachable = Math.max(reachable, i+nums[i]);
        }
        return true;
    }
}

// @lc code=end
