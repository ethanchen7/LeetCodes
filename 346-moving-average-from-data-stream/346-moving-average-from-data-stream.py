class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.capacity = size

    def next(self, val: int) -> float:
        if len(self.queue) >= self.capacity:
            self.queue.popleft()
        self.queue.append(val)
        
        total = 0
        for num in self.queue:
            total += num
        
        return total / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)