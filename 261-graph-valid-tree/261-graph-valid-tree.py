class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
        
        def find(x):
            if self.parents[x] != x:
                self.parents[x] = find(self.parents[x])
            
            return self.parents[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False
            
            if self.rank[root_x] == self.rank[root_y]:
                self.parents[root_y] = root_x
                self.rank[root_x] += 1
            
            elif self.rank[root_y] > self.rank[root_x]:
                self.parents[root_x] = root_y
            
            else:
                self.parents[root_y] = root_x
            
            return True
        
        for x, y in edges:
            if not union(x, y):
                return False
        
        # the case that not all nodes are connected
        # we can check because there should only be one parent root node
        
        parent = set()
        for node in self.parents:
            parent.add(find(node))
        
        if len(parent) > 1:
            return False
        return True