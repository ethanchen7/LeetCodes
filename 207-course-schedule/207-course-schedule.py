class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adjList = collections.defaultdict(list)
        
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        #DFS
        visited = set()
        def cycle(course):
            
            if course in visited:
                return True
            
            if not adjList[course]:
                return False
            
            visited.add(course)
            for pre in adjList[course]:
                if cycle(pre): 
                    return True
                
            visited.remove(course)
            adjList[course] = []
            return False
                
        for i in range(numCourses):
            if cycle(i):
                return False
        
        return True