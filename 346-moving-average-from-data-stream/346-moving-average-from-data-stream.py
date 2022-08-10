class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.capacity = size

    def next(self, val: int) -> float:
        if len(self.queue) >= self.capacity:
            prev, old_total = self.queue.popleft()
            if self.queue:
                self.queue[-1][1] -= prev
            
        if not self.queue:
            self.queue.append([val, val])
            return self.queue[-1][1] / len(self.queue)
        
        prev_sum = self.queue[-1][1]
        new_sum = prev_sum + val
        self.queue.append([val, new_sum])
        return new_sum / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)