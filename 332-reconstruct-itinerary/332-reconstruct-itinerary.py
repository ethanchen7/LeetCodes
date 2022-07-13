class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort() # will sort by pair in lexical order
        
        graph = collections.defaultdict(list)
        for ticket in tickets:
            source, dest = ticket[0], ticket[1]
            graph[source].append(dest)
        
        res = ["JFK"]
        def dfs(src):
            
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in graph:
                return False
            
            for idx, vertex in enumerate(graph[src]):
                res.append(vertex)
                graph[src].pop(idx)
                result = dfs(vertex)
                if result:
                    return True
                
                graph[src].insert(idx,vertex)
                res.pop()
            
            return False
        
        dfs("JFK")
        return res