"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

"""
As we go through the possible ways of reaching a particular endWord from a beginWord. We can see that it forms a tree.

Example:

beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

        hit----hot----dot----dog----log
                \              \\
                 \----lot       \---*cog*
                       \             
                        \----log----*cog*
So why not create a tree structure that can store these values and just transverse the tree to get the results we want.

"""
import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
		# A TreeNode class that can form part of N-ary tree structure
        class TreeNode:
            def __init__(self, val):
                self.val = val
                self.children = []
            
            def addChild(self, node):
                self.children.append(node)
            
            def getChildren(self):
                return self.children
                
        # Check if the endWord is in the wordList, if it isn't, then it is impossible to achieve that word
		# So return empty list
        if endWord not in wordList:
            return []
        
		# This uses the same idea as Word Ladder I official solution
		# Create a dictionary that contains intermediate words as keys and actual words as the values
        comboMap = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(len(beginWord)):
                comboMap[word[:i] + "*" + word[i+1:]].append(word)
                
        
        deque = collections.deque()
		
		# Visited set is used to prevent cycles
        visited = set()
		
		# Instead of using (word, level) pair, we are using (word, parent_node) pair
		# This is done to easily access the parent node in the queue and create the tree structure
        deque.append((beginWord, None))
        root = None

        while deque:
            currword, parent = deque.popleft()
		
			# Create a TreeNode with the current word as the value
            node = TreeNode(currword)
            
			# If the word's pair (i.e. the parent node) is not None
			# -> We can add this node as the child to that parent
			# else
			# -> We make the node the root node
            if parent:
                parent.addChild(node)
            else:
                root = node                         
            
			# If the currword is the endWord then no need to go past it, as this would only add combinations
			# greater in length
			# Therefore continue the loop
            if currword == endWord:
                continue
            
			# We add the currword to the visited set
            visited.add(currword)
            for i in range(len(currword)):
				# Generate our intermediate word and add all of the words that are
				# reachable from our intermediate word
                interword = currword[:i] + "*" + currword[i+1:]
                
                for word in comboMap[interword]:
                    if word not in visited:
                        deque.append((word, node))
        
        res = []
        
		# Function that will travserse the tree we created and add to our res (result) list
        def traverseTree(root, curr):
            nonlocal res
            if root is None:
                return
            
            curr.append(root.val)
            
            if len(root.getChildren()) == 0 and root.val == endWord:
				# If the length of res is 0, then we can add the curr list
                if len(res) == 0:
                    res.append(curr[:])
				# If the length of the first element of res is equal to the length of the curr list
				# This is another valid way of reaching the endWord, therefore add to res
                elif len(res[0]) == len(curr):
                    res.append(curr[:])
				# If the length of the first element of res is greater than the length of curr list
				# We know that all of the elements of res would be also greater than the lenght of curr list
				# Therefore create new list and append curr list 
                elif len(res[0]) > len(curr):
                    res = []
                    res.append(curr[:])
                    
            # Recursively traverse the children
            for child in root.getChildren():
                traverseTree(child, curr)
			
            curr.pop()
        
        traverseTree(root,[])
        
		# Finally return our res (result) list
        return res