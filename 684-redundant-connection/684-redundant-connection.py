class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        res = None
        
        parents = [i for i in range(len(edges) + 1)]
        ranks = [1 for i in range(len(edges) + 1)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            
            return parents[x]
        
        def union(x, y):
            nonlocal res
            
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                res = [x, y]
            
            if ranks[root_x] >= ranks[root_y]:
                parents[root_y] = root_x
                ranks[root_x] += ranks[root_y]
            
            else:
                parents[root_x] = root_y
                ranks[root_y] += ranks[root_x]
        
        for x, y in edges:
            union(x, y)
        
        return res