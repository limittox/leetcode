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
        # The length and widths of the grid
        N = len(grid[0])
        M = len(grid)
        queue = []
        
        # This is used later to more easily check the neighbouring grid squares
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        minute = -1
        orange_count = 0
        
        # Adding rotten oranges to queue and find the number of fresh orange on the grid
        for row in range(M):
            for col in range(N):
                if grid[row][col] == 2:
                    queue.append([row, col])
                if grid[row][col] == 1:
                    orange_count += 1


        if not queue and orange_count:
            return -1
        elif queue: # This is to indicate when an iteration is over
            queue.append([-1,-1])

        # BFS
        while queue:
            curr = queue.pop(0)
            
            i, j = curr
            
            # Add an indicator to the end to indicate another end of an iteration
            if queue and i == -1:
                queue.append([-1,-1])
                
            if i == -1:
                minute += 1
                continue
            
            for c, mod in enumerate(directions):
                modi, modj = mod
                row = i+modi
                col = j+modj
                
                if not (row >= 0 and row < M and col >= 0 and col < N):
                    continue
                
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    orange_count -= 1
                    queue.append([row, col])
                    
            
                

        return max(0,minute) if orange_count == 0 else -1