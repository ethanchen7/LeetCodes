class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = [i for i in range(0, len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            
            return parents[node]
        
        def union(node1, node2):
            root_one = find(node1)
            root_two = find(node2)
            
            if root_one == root_two:
                return False
            
            if rank[root_one] == rank[root_two]:
                parents[root_two] = node1
                rank[root_one] += 1
            
            elif rank[root_two] > rank[root_one]:
                parents[root_one] = root_two
                rank[root_two] += 1
            
            else:
                parents[root_two] = root_one
                
            return True 
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
            