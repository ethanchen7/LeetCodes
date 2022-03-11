class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # indegrees are nodes that don't have nodes pointing to it.
        # store the nodes that have pointers to them in a hashmap, return all the ones that are not in the hashmap
        
        indegrees = {}
        
        for n1, n2 in edges:
            if n2 in indegrees:
                indegrees[n2] += 1
            else:
                indegrees[n2] = 1
        
        result = []
        
        for i in range(n):
            if i not in indegrees:
                result.append(i)
        
        return result