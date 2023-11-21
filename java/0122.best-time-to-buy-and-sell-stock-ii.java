// Created by Eddie Ho at 2023/11/17 17:05
// leetgo: 1.3.8
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

// @lc code=begin

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i-1]) {
                profit += prices[i] - prices[i-1];
            }
        }
        return profit;
    }
}

// @lc code=end
