class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)
        heap = []
        for key in counter:
            heappush(heap, -counter[key])
        
        queue = deque()
        
        time = 0
        while heap or queue:
            
            if heap:
                count = heappop(heap)
                if count < -1:
                    queue.append((count + 1, time + n)) # available at current time + idle time
            
            if queue and queue[0][1] == time:
                cnt, tm = queue.popleft()
                heappush(heap, cnt)
            
            time += 1
        
        return time
            
                