"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

Question: https://leetcode.com/problems/longest-common-subsequence/
"""
# M and N are the lengths of the strings
# Time: 2^L
# Space: ???
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def helper(text1, text2):
            if not text1 or not text2:
                return 0
            
            if text1[0] == text2[0]:
                return helper(text1[1:], text2[1:]) + 1
            
            return max(helper(text1[1:], text2), helper(text1, text2[1:]))
        
        return helper(text1, text2)
        
# M and N are the lengths of the strings
# Time: O(M*N)
# Space: O(M*N)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for i in range(len(text2)+1)] for i in range(len(text1)+1)]
        def helper(t1, t2):
            if t1 == len(text1) or t2 == len(text2):
                return 0
            
            if memo[t1+1][t2+1] != 0:
                return memo[t1+1][t2+1]
            
            if text1[t1] == text2[t2]:
                memo[t1+1][t2+1] = helper(t1+1, t2+1) + 1
                return memo[t1+1][t2+1]
            
            memo[t1+1][t2+1] = max(helper(t1+1, t2), helper(t1, t2+1))
            return memo[t1+1][t2+1]

        return helper(0, 0)

# M and N are the lengths of the strings
# Time: O(M*N)
# Space: O(M*N)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            a b c d e
          0 0 0 0 0 0
        a 0 1 1 1 1 1
        c 0 1 1 2 2 2
        e 0 1 1 2 2 3
        """
        
        dp = [[0 for i in range(len(text2)+1)] for i in range(len(text1)+1)]
        # rows would be represented by text1
        # cols would be represented by text2
        for r in range(1,len(dp)):
            for c in range(1,len(dp[0])):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1]+1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]

# M and N are the lengths of the strings
# Time: O(M*N)
# Space: O(min(M,N))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        previous = [0 for i in range(len(text2)+1)]
        current = [0 for i in range(len(text2)+1)]

        # rows would be represented by text1
        # cols would be represented by text2
        for r in range(1,len(text1)+1):
            # current = [0 for i in range(len(text2)+1)]
            for c in range(1,len(text2)+1):
                if text1[r-1] == text2[c-1]:
                    current[c] = previous[c-1]+1
                else:
                    current[c] = max(current[c-1], previous[c])
            previous, current = current, previous
        return previous[-1]
