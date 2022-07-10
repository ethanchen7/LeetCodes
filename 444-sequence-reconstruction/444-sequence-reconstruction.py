class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        
        sorted_order = []
        
        graph = {i + 1: [] for i in range(len(nums))}
        inDegrees= {i+1: 0 for i in range(len(nums))}
        
        for i in range(len(sequences)):
            for j in range(0, len(sequences[i]) - 1):
                parent, child = sequences[i][j], sequences[i][j+1]
                graph[parent].append(child)
                inDegrees[child] += 1
        
        sources = collections.deque()
        for key in inDegrees:
            if inDegrees[key] == 0:
                sources.append(key)
        
        while sources:
            if len(sources) > 1:
                return False
            
            if sources[0] != nums[len(sorted_order)]:
                return False
            
            source = sources.popleft()
            sorted_order.append(source)
            for child in graph[source]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    sources.append(child)
        
        return len(sorted_order) == len(nums)
        