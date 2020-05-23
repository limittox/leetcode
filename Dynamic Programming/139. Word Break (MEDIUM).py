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
#-------SOLUTION------
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