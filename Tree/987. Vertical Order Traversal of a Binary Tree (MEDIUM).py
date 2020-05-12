"""Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:
              3
            /   \
           9    20
               /  \
              15   7

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
 
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My solution
# Time: O(Nlog(N/k)), Space: O(N)
import sys, collections
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes_map = collections.defaultdict(list)
        vpos_min = sys.maxsize
        vpos_max = -sys.maxsize
        
        def helper(root, vpos, hpos):
            nonlocal vpos_min, vpos_max
            if root is None:
                return
            
            vpos_min = min(vpos_min, vpos)
            vpos_max = max(vpos_max, vpos)
            
            while len(nodes_map[vpos]) <= hpos:
                nodes_map[vpos].append([])
            
            nodes_map[vpos][hpos].append(root.val)
                
            helper(root.left, vpos-1, hpos+1)
            helper(root.right, vpos+1, hpos+1)
        
        helper(root, 0, 0)
        res = []
        
        for key in nodes_map:
            for i in range(len(nodes_map[key])):
                nodes_map[key][i].sort()

        for i in range(vpos_min, vpos_max+1):
            curr_res = []
            for values in nodes_map[i]:
                for val in values:
                    curr_res.append(val)
            res.append(curr_res)
        
        
        return res

"""
A better solution would be to store (hpos, val) pairs in the hashmap, 
then sort them right before outputting them. Might make the complexity 
of the code bit easier to write. vpos_min and vpos_max can also be
intialised to 0 at the start instead.

Another solution with worse time complexity would be to store,
(vpos, hpos, val) triplets in a res list. Then sort this list,
Then return a list created by grouping vpos vals together.
However this solution has worse complexity.
"""