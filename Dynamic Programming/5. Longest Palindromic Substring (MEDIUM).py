"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
https://leetcode.com/problems/longest-palindromic-substring/
"""
# O(N^2) and constant space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCorner(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return r-l-1
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = expandAroundCorner(s, i, i)
            len2 = expandAroundCorner(s, i, i+1)
            lenMax = max(len1, len2)
            if lenMax > end - start:
                start = i - ((lenMax-1)//2)
                end = i + lenMax//2
            
        return s[start:end+1]
