"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Pre-order: root, left, right
        Inorder: left, root, right
        """
        
        if len(preorder) == 0 or len(inorder) == 0:
            return
        
        val = preorder[0]
        root = TreeNode(val)
        
        root_id = 0
        for i, v in enumerate(inorder):
            if val == v:
                root_id = i
        
        
        
        root.left = self.buildTree(preorder[1:root_id+1], inorder[:root_id])
        root.right = self.buildTree(preorder[root_id+1:], inorder[root_id+1:])
        
        return root