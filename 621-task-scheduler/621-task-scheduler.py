class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_map = Counter(tasks)
        maxHeap = [-task_map[count] for count in task_map]
        heapify(maxHeap)
        
        queue = deque()
        time = 0
        while maxHeap or queue:
            
            time += 1
            
            if maxHeap:
                count =  1 + heappop(maxHeap)
                if count:
                    queue.append((count, time + n))
            
            if queue and queue[0][1] == time:
                count, t = queue.popleft()
                heappush(maxHeap, count)
        
        return time