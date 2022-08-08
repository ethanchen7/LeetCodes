class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        parents = [i for i in range(n + 1)]
        ranks = [1 for i in range(n + 1)]
        
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
        
        connections.sort(key=lambda x: x[2]) # sort by cost
        # [2,3,1], [1,2,5], [1,3,6]
        result = 0
        count = 0
        
        for n1, n2, dist in connections:
            if union(n1, n2):
                result += dist
                count += 1
        
        if count == n - 1:
            return result
        
        return -1
            