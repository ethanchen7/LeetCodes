class ExamRoom:
    
    def calc_segment(self, x, y): # this calculates the available segment length
        if x == -1: # the first available seat is 0, so the max distance rn is 10
            return -y
        elif y == self.N: 
            return -(self.N - x - 1)
        else:
            return -(abs(x-y)//2) 

    def __init__(self, n: int):
        self.N = n
        self.heapq = [(self.calc_segment(-1, self.N), -1, self.N)] # initialize the heap, biggest segments are priority
    
    def seat(self) -> int:
        
        dist, x, y = heappop(self.heapq) # max seat interval at any point
        seat = None
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x + y) // 2
        
        heappush(self.heapq, (self.calc_segment(x, seat), x, seat)) #push the available segments onto the heap, break at the seat
        heappush(self.heapq, (self.calc_segment(seat, y), seat, y))
        return seat        

    def leave(self, p: int) -> None:
        head = tail = None # two pointers, delete the intervals related to that seat
        # ex: 0 2 4    9 (deleting 4)
        # right now we have two intervals relating to seat 4.
        # (-2, 4, 9), (-1, 2, 4)
        #     T            H
        print(self.heapq)
        for interval in self.heapq: # (d, u, v)
            if interval[1] == p:
                tail = interval
            if interval[2] == p:
                head = interval
            if head and tail:
                break
                
        self.heapq.remove(head) # remove the intervals
        self.heapq.remove(tail)
        heapify(self.heapq) # must heapify again
        heappush(self.heapq, (self.calc_segment(head[1], tail[2]), head[1], tail[2]))

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)