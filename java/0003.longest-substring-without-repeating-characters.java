// Created by Eddie Ho at 2023/11/13 11:32
// leetgo: 1.3.8
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

// @lc code=begin

import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> counter = new HashMap<>();
        int output = 0;
        int minIdx = 0;

        for (int i = 0; i < s.length(); i++) {
            if (counter.containsKey(s.charAt(i))) {
                minIdx = Math.max(minIdx, counter.get(s.charAt(i)) + 1);
            }

            output = Math.max(output, i - minIdx + 1);
            counter.put(s.charAt(i), i);
        }

        return output;
    }
}

// @lc code=end
