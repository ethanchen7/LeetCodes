class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        parents = [i for i in range(len(isConnected))]
        ranks = [1 for i in range(len(isConnected))]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            
            return parents[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return
            
            if ranks[root_x] >= ranks[root_y]:
                parents[root_y] = root_x
                ranks[root_x] += ranks[root_y]
            else:
                parents[root_x] = root_y
                ranks[root_y] += ranks[root_x]
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        parent_set = set()
        for p in parents:
            parent_set.add(find(p))
        
        return len(parent_set)