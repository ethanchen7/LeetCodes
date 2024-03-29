class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parents = [i for i in range(n)]
        ranks = [1 for i in range(n)]
        
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
        
        for x, y in edges:
            union(x, y)
        
        for i, p in enumerate(parents):
            parents[i] = find(p)
        
        return len(set(parents))