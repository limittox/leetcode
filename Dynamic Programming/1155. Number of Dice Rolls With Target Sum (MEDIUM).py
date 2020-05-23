"""
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""
#--------SOLUTION-------------------------------

"""
d number of dice
f number of sides (1 to f inclusive)
target that I have to reach

dp = d+1 number of rows and target+1 number of cols
-----------------------------------------------------
Eg 1:
d = 1, f = 6, target = 6

d----target-----
    0 1 2 3 4 5 6
0[1,0,0,0,0,0,0]
1[0,1,1,1,1,1,1]

-----------------------------------------------------
Eg 2:
d = 2, f = 6, target = 7

d-----target-----
    0 1 2 3 4 5 6 7
0[1,0,0,0,0,0,0,0]
1[0,1,1,1,1,1,1,0]
2[0,0,1,2,3,4,5,6]
3[0,0,0,1,3,6,10,15]

"""

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        
        dp[0][0] = 1
        
        for r in range(1, d+1):
            for c in range(1, target+1):
                for b in range(1, f+1):
                    if (c-b) >= 0:
                        dp[r][c] = (dp[r][c] + dp[r-1][c-b])%(10**9+7)
        return dp[-1][-1]