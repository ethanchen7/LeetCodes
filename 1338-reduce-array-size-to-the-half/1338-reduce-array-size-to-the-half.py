class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        c = Counter(arr)
        
        heap = [[-c[n], n] for n in c]
        heapify(heap)
        
        target_length = len(arr) // 2
        
        min_amount = math.inf
        
        size = 0
        count = 0
        while heap:
            
            sz, num = heappop(heap)
            size -= sz
            count += 1
            
            if size >= target_length:
                min_amount = min(min_amount, count)
                size += sz
                count -= 1
        
        return min_amount