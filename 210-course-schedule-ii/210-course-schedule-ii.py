class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        sorted_order = []
        
        if numCourses <= 0:
            return sorted_order
        
        graph = {i: [] for i in range(numCourses)}
        inDegrees = {i: 0 for i in range(numCourses)}
        
        for relation in prerequisites:
            parent, child = relation[0], relation[1]
            graph[parent].append(child)
            inDegrees[child] += 1
        
        sources = collections.deque()
        for child in inDegrees:
            if inDegrees[child] == 0:
                sources.append(child)
        
        while sources:
            source = sources.popleft()
            sorted_order.append(source)
            for child in graph[source]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    sources.append(child)
        
        if len(sorted_order) != numCourses:
            return []
        
        return sorted_order[::-1]
        