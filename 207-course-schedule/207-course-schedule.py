class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        sorted_order = []
        
        graph = {i: [] for i in range(numCourses)} 
        inDegrees = {i:0 for i in range(numCourses)}
        
        for crs, dep in prerequisites:
            graph[crs].append(dep)
            inDegrees[dep] += 1
        
        sources = deque()
        for key in inDegrees:
            if inDegrees[key] == 0:
                sources.append(key)
        
        while sources:
            source = sources.popleft()
            sorted_order.append(source)
            
            for vertex in graph[source]:
                inDegrees[vertex] -= 1
                if inDegrees[vertex] == 0:
                    sources.append(vertex)
        
        if len(sorted_order) != numCourses:
            return False
        
        return True