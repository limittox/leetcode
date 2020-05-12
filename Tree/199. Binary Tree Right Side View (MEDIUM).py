"""Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) Time and Space
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        
        def helper(root, level):
            if root is None:
                return
            
            if len(res) == level:
                res.append(root.val)
            
            helper(root.right, level+1)
            helper(root.left, level+1)
        
        helper(root, 0)

        return res