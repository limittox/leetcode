"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        oranges = 0
        M = len(grid)
        N = len(grid[0])
        
        directions = ((-1,0), (0,-1), (1,0), (0,1))
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        queue.append((-1,-1))
        
        minutes = -1
        while queue:
            r, c = queue.popleft()
            
            if r == -1:
                if queue:
                    queue.append((-1,-1))
                minutes += 1
                continue
            
            for dirr, dirc in directions:
                modr = r+dirr
                modc = c+dirc
                
                if modr >= 0 and modr < M and modc >=0 and modc < N:
                    if grid[modr][modc] == 1:
                        grid[modr][modc] = 2
                        queue.append((modr,modc))
                        oranges -= 1
        
        return minutes if oranges == 0 else -1
