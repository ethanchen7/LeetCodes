class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        c = Counter(tasks)
        heap = [[-c[char], char] for char in c]
        heapify(heap)
        
        queue = deque()
        
        time = 0
        while heap or queue:
            
            if heap:
                freq, char = heappop(heap)
                if freq < -1:
                    queue.append([freq + 1, char, time + n])
            
            if queue and queue[0][2] == time:
                f, c, t = queue.popleft()
                heappush(heap, [f, c])
            
            time += 1
            
        return time