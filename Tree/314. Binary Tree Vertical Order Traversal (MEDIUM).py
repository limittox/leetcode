"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My solution
# O(N) Time and Space
import collections
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        res = collections.defaultdict(list)
        vmin = vmax = 0
        
        def helper(root, vpos, hpos):
            nonlocal vmin, vmax
            if root is None:
                return
            
            vmin = min(vmin, vpos)
            vmax = max(vmax, vpos)
            
            while len(res[vpos]) <= hpos:
                res[vpos].append([])
            
            
            res[vpos][hpos].append(root.val)
            helper(root.left, vpos-1, hpos+1)
            helper(root.right, vpos+1, hpos+1)
        
        helper(root, 0, 0)
        
        output = []

        for i in range(vmin, vmax+1):
            curr_vpos = []
            for values in res[i]:
                for val in values:
                    curr_vpos.append(val)
            
            output.append(curr_vpos)
        return output