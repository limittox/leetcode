class Solution:
    time = 0
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # Creates a graph based on connections
        def makeGraph(connections):
            graph = collections.defaultdict(list)
            for a, b in connections:
                graph[a].append(b)
                graph[b].append(a)
            return graph
        
        graph = makeGraph(connections)
        
        visitedTime = [0 for _ in range(len(graph))]
        lowTime = [0 for _ in range(len(graph))]
        
        res = []
        
        """
        We visit every node on the graph and we assign a visited time for them and a lowtime.
        Visited time says the depth of that node from the start node.
        Low time says the the lowest low time of neighbours.

        If a node which is a neighbour of the current node has a smaller low_time than
        """
        def dfs(currNode, parentNode, visited):
            visited.add(currNode)
            self.time += 1
            visitedTime[currNode] = self.time
            lowTime[currNode] = self.time
            
            neighbours = graph[currNode]
            for neighbour in neighbours:
                if neighbour == parentNode:
                    continue
                if neighbour not in visited:
                    dfs(neighbour, currNode, visited)
                    lowTime[currNode] = min(lowTime[currNode], lowTime[neighbour])
                    if visitedTime[currNode] < lowTime[neighbour]:
                        res.append([currNode, neighbour])
                else:
                    lowTime[currNode] = min(lowTime[currNode], lowTime[neighbour])
                    
        
        dfs(0, -1, set())
        return res