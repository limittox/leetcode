"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        def dfs(grid, row, col):
            rows = len(grid)
            cols = len(grid[0])
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            if row < rows and row >= 0 and col < cols and col >= 0:
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    for r, c in directions:
                        dfs(grid, row+r, col+c)
        
        res = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    res += 1
                    dfs(grid, row, col)
        return res