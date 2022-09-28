class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}
        inDegrees = {i: 0 for i in range(numCourses)}
        
        for x, y in prerequisites:
            graph[x].append(y)
            inDegrees[y] += 1
        
        sources = deque()
        for node in inDegrees:
            if inDegrees[node] == 0:
                sources.append(node)
        
        sorted_order = []
        while sources:
            
            source = sources.popleft()
            sorted_order.append(source)
            
            for n in graph[source]:
                inDegrees[n] -= 1
                if inDegrees[n] == 0:
                    sources.append(n)
        
        return True if len(sorted_order) == numCourses else False