"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        words = set(wordDict)
        def checkWordBreak(s, words=words):
            dp = [False for _ in range(len(s)+1)]

            dp[0] = True

            for i in range(len(s)):
                for j in range(i+1, len(s)+1):
                    if s[i:j] in words and dp[i] == True:
                        dp[j] = True

            return dp[-1]
            
        
        def helper(s, words, curr):
            if not checkWordBreak(s):
                return
            
            if len(s) == 0:
                res.append(curr[:-1])
                return
            
            for j in range(1, len(s)+1):
                if s[:j] in words:
                    helper(s[j:], words, curr+s[:j]+" ")
                        
        helper(s, words, "")
        return res

# Very similar way, without using a string for curr (might improve complexity)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        def isWordBreak(s):
            dp = [False for i in range(len(s)+1)]
            dp[0] = True
            
            for i in range(len(s)):
                for j in range(len(s)+1):
                    if dp[i] and s[i:j] in wordDict:
                        dp[j] = True
            
            return dp[-1]
        res = []
        def dfs(s, curr):
            if not s:
                res.append(' '.join(curr[:]))
                return
            
            if not isWordBreak(s):
                return
            
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    curr.append(s[:i])
                    dfs(s[i:], curr)
                    curr.pop()
        dfs(s, [])
        
        return res