// Created by Eddie Ho at 2023/11/17 10:43
// leetgo: 1.3.8
// https://leetcode.com/problems/rotate-array/

// @lc code=begin

class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        _rotate(nums, 0, n-k);
        _rotate(nums, n-k, n);
        _rotate(nums, 0, n);
    }

    private void _rotate(int[] nums, int start, int stop) {
        while (start < stop) {
            int temp = nums[start];
            nums[start] = nums[stop-1];
            nums[stop-1] = temp;
            start++;
            stop--;
        }
    }
}

// @lc code=end
