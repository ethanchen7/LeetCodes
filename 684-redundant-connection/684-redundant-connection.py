class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        self.parents = [i for i in range(len(edges) + 2)]
        self.ranks = [1] * (len(edges) + 1)
        
    
        def find(x):
            if not self.parents[x] == x:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False
            
            if self.ranks[root_x] > self.ranks[root_y]:
                self.parents[root_y] = root_x
                self.ranks[root_x] += 1
            
            elif self.ranks[root_y] > self.ranks[root_x]:
                self.parents[root_x] = root_y
            
            else:
                self.parents[root_y] = root_x
            
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x,y]
            