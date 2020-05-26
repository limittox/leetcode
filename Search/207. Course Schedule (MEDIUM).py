"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""

       
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Some courses that you need to take.
        
        [0,1] - 1 is a pre-req to 0. i.e. You need to take  1 before you can take 0
        
        Need to finish all courses, given by numCourses
        
        Solution:
        
        Need to detect cycles in the graph
        -- Visited set that records all of the nodes that we have visited
        -- return len(visited) == numCourses
        
        {
            0: [],
            1: [2],
            2: [1],
            3: [2,0]
        }
        
        {
            0: [],
            1: [0],
            2: [0,1],
            3: [2,0]
        }
        
        {
            0: [1],
            1: [0]
        }
        
        3----->2---->1
         \     |     |
          \    v     |
           \-->0<----|
        
        
        """
        relations = collections.defaultdict(list)
        
        for course, prereq in prerequisites:
            relations[prereq].append(course)
            if course not in relations:
                relations[course] = []
        
        visited = set()
        checked = set()
        ret = []
        
        def dfs(course, visited, checked):
            if course in checked:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            for nextCourse in relations[course]:
                if nextCourse in visited:
                    return False
                if not dfs(nextCourse, visited, checked):
                    return False
                
            checked.add(course)
            ret.append(course)
            visited.remove(course)
            return True
        
        courses = list(relations.keys())
        for course in courses:
            if not dfs(course, visited, checked):
                return False

        return True
            