class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
        
        def find(node):
            if self.parents[node] != node:
                self.parents[node] = find(self.parents[node])
            return self.parents[node]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if self.rank[root_x] == self.rank[root_y]:
                self.parents[root_y] = root_x
                self.rank[root_x] += 1
            
            elif self.rank[root_y] > self.rank[root_x]:
                self.parents[root_x] = root_y
            
            else:
                self.parents[root_y] = root_x
        
        for x, y in edges:
            union(x, y)
        
        parents = set()
        for p in self.parents:
            parents.add(find(p))
        
        return len(parents)
            