class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        
        graph = collections.defaultdict(list)
        for source, dest in tickets:
            graph[source].append(dest)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            for i, v in enumerate(graph[src]):
                res.append(v)
                graph[src].pop(i)
                result = dfs(v)
                if result:
                    return True
                res.pop()
                graph[src].insert(i, v)
        
        dfs("JFK")
        return res