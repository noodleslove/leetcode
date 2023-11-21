// Created by Eddie Ho at 2023/11/18 23:51
// leetgo: 1.3.8
// https://leetcode.com/problems/jump-game-ii/

// @lc code=begin

import java.util.Arrays;

class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1, n, Integer.MAX_VALUE);

        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= nums[i]; j++) {
                if (i + j >= n) {
                    break;
                }
                dp[i + j] = Math.min(dp[i] + 1, dp[i + j]);
            }
        }

        return dp[n - 1];
    }
}

// @lc code=end
