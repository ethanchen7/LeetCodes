# hash map and sort by timestamp
class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        grans = {'Year': 5, 'Month': 8, 'Day': 11, 'Hour': 14, 'Minute': 17, 'Second': 20}
        result = []
        for t, i in sorted(self.logs):
            spec = grans[granularity]
            if start[:spec] <= t[:spec] <= end[:spec]:
                result.append(i)
        
        return result
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)