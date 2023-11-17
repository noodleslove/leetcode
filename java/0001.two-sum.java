// Created by Eddie Ho at 2023/11/12 22:49
// leetgo: 1.3.8
// https://leetcode.com/problems/two-sum/

// @lc code=begin
import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            if (seen.containsKey(nums[i])) {
                return new int[]{seen.get(nums[i]), i};
            }
            seen.put(target - nums[i], i);
        }

        return new int[]{-1, -1};
    }
}

// @lc code=end
