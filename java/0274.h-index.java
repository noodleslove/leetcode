// Created by Eddie Ho at 2023/11/19 01:34
// leetgo: 1.3.8
// https://leetcode.com/problems/h-index/

// @lc code=begin

import java.util.*;

class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int _hIndex = Integer.MIN_VALUE;
        Arrays.sort(citations);
        
        for (int i = n - 1; i >= 0; i--) {
            int h = Math.min(n - i, citations[i]);
            _hIndex = Math.max(_hIndex, h);
        }
        return _hIndex;
    }
}

// @lc code=end
