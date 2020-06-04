"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
#-------SOLUTION------#
# Recursion
# N is the length of the String s
# Time: O(2^N) **TLE**
# Space: O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        s = leetcode
        wordDict = ["leet", "code"]
        --> True
        
        s[0:4] == "leet"
        s[4:8] == "code"
        ___________________________________
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        --> True
        ___________________________________
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        --> False
        ___________________________________
        s = "catsanddog"
        wordDict = ["cats", "dog", "and", "cat"]
        --> True
        
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        [1,0,0,1,1,0,0,1,0,0,1]
        
        return dp[-1]
        
        """
        wordDict = set(wordDict)
        def backtrack(s):
            if not s:
                return True
            
            for i in range(1,len(s)+1):
                if s[:i] in wordDict and backtrack(s[i:]):
                    return True
            
            return False
        
        return backtrack(s)

# Recursion with Memoization
# N is the length of the String s
# Time: O(N^2)
# Space: O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = [-1 for i in range(len(s))]

        def backtrack(start):
            if start == len(s):
                return True
            
            if memo[start] != -1:
                return memo[start]
            
            for i in range(start+1,len(s)+1):
                if s[start:i] in wordDict and (backtrack(i)):
                    memo[start] = True
                    return memo[start] 
                
            memo[start] = False
            return memo[start]

        return backtrack(0)

# N is the length of the String s
# Dynamic Programming
# Time: O(N^2)
# Space: O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        catsandog
        catsanddog
        ["cats", "dog", "sand", "and", "cat"]
        
        c a t s a n d o g
        T     T T     T
        
        c a t s a n d d o g
        T     T T     T   T
        
        leetcode
        ["leet", "code"]
        
        l e e t c o d e
        T       T       T
        
        dp = initialized to all False, size of len(s)+1
        dp[0] = True
        
        Iterate through the string with a nested loop, and check if the substrings
        where the indices lie, are words.
                --> YES
                    --> dp[j+1] = True (where j is the end of the substring)
                --> NO
                    --> keep going
        """
        words = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] in words and dp[i] == True:
                    dp[j] = True

        return dp[-1]