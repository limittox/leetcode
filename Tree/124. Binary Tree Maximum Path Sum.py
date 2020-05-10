# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
"""
       1
      / \
     2   3
    / \
   3  -1
   = 3+2+1+3
   = 9
       1
      / \
    -2   3
    / \
   3  -1
   = 4
      -1
      / \
    -2   2
    / \
   3  -1
   = 3
"""
import sys
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = -sys.maxsize
        def helper(root):
            nonlocal maxSum
            if root is None:
                return -sys.maxsize
            
            L = helper(root.left)
            R = helper(root.right)
            maxL = max(L, 0)
            maxR = max(R, 0)
            
            
            path_sum = root.val + maxL + maxR
            
            maxSum = max(maxSum, path_sum, L, R)
            
            return root.val + max(maxL, maxR)
        
        helper(root)

        return maxSum