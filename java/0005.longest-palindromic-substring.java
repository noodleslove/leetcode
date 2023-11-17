// Created by Eddie Ho at 2023/11/13 16:44
// leetgo: 1.3.8
// https://leetcode.com/problems/longest-palindromic-substring/

// @lc code=begin

class Solution {
    int maxLength = 0;
    int start = 0;

    public String longestPalindrome(String s) {
        var input = s.toCharArray();
        if (input.length < 2) {
            return s;
        }

        for (int i = 0; i < input.length; i++) {
            expandPalindrome(input, i, i); // odd palindrome
            expandPalindrome(input, i, i + 1); // even palindrome
        }

        return s.substring(start, start + maxLength);
    }

    private void expandPalindrome(char[] s, int left, int right) {
        while (left >= 0 && right < s.length && s[left] == s[right]) {
            left--;
            right++;
        }

        if (maxLength < right - left - 1) {
            maxLength = right - left - 1;
            start = left + 1;
        }
    }
}

// @lc code=end
