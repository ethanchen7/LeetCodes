class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = [i for i in range(len(edges))]
        ranks = [1 for i in range(len(edges))]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False
            
            if ranks[root_x] >= ranks[root_y]:
                parents[root_y] = root_x
                ranks[root_x] += ranks[root_y]
            
            else:
                parents[root_x] = root_y
                ranks[root_y] += ranks[root_x]
            
            return True
        
        res = None
        
        for x, y in edges:
            if not union(x - 1, y - 1):
                res = [x, y]
        
        return res
        