// Created by Eddie Ho at 2023/11/17 00:16
// leetgo: 1.3.8
// https://leetcode.com/problems/majority-element/

// @lc code=begin

import java.util.Arrays;

class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}

// @lc code=end
