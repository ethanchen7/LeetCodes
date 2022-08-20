class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        # create new groups for the items with no group
        for i, g in enumerate(group):
            if g == -1:
                group[i] = m
                m += 1
        
        # two graphs, one for groups, one for items
        # we will sort the groups and sort the items 
        groups = {i: [] for i in range(m)}
        groupsIndegrees = {i: 0 for i in range(m)}
        items = {i: [] for i in range(n)}
        itemsIndegrees = {i: 0 for i in range(n)}
        
        for i in range(n):
            for v in beforeItems[i]: # create item relationships
                items[v].append(i)
                itemsIndegrees[i] += 1
                
                if group[i] != group[v]: # create group relationships
                    groups[group[v]].append(group[i])
                    groupsIndegrees[group[i]] += 1
        
        groups_top_sort = self.topo_sort(groups, groupsIndegrees)
        items_top_sort = self.topo_sort(items, itemsIndegrees)
        if not groups_top_sort or not items_top_sort: return []
        
        # find ordering of items within groups 
        group_item_order = collections.defaultdict(list)
        for i in items_top_sort:
            group_item_order[group[i]].append(i)
        
        res = []
        for g in groups_top_sort:
            res += group_item_order[g]
        return res
        
    def topo_sort(self, graph, inDegree):
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
                
        sorted_order = []
        while sources:
            source = sources.popleft()
            sorted_order.append(source)
            
            for node in graph[source]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    sources.append(node)
        
        return sorted_order if len(sorted_order) == len(inDegree) else []
        
        