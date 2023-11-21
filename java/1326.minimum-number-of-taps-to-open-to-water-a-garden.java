// Created by Eddie Ho at 2023/11/18 17:04
// leetgo: 1.3.8
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

// @lc code=begin

import java.util.Arrays;

class Solution {
    public int minTaps(int n, int[] ranges) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 1, n + 1, Integer.MAX_VALUE);

        for (int i = 0; i < n + 1; i++) {
            int start = Math.max(0, i - ranges[i]);
            int end = Math.min(n, i + ranges[i]);
            for (int j = start + 1; j < end + 1; j++) {
                dp[j] = Math.min(dp[start] + 1, dp[j]);
            }
        }

        return dp[n] != Integer.MAX_VALUE ? dp[n] : -1;
    }
}

// @lc code=end
