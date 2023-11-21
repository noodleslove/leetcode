// Created by Eddie Ho at 2023/11/17 10:57
// leetgo: 1.3.8
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

// @lc code=begin

class Solution {
    public int maxProfit(int[] prices) {
        int left = 0, right = 1;
        int _maxProfit = 0;
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                _maxProfit = Math.max(_maxProfit, prices[right] - prices[left]);
            } else {
                left = right;
            }
            right++;
        }
        return _maxProfit;
    }
}

// @lc code=end
