"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.  
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                dp[r][c] += grid[r][c]
                
                if r > 0 and c > 0:
                    dp[r][c] += min(dp[r][c-1], dp[r-1][c])
                elif r > 0:
                    dp[r][c] += dp[r-1][c]
                elif c > 0:
                    dp[r][c] += dp[r][c-1]
        
        return dp[len(grid)-1][len(grid[0])-1]