class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        
        if key not in self.map:
            return res
        
        objects = self.map[key]
        left = 0
        right = len(objects) - 1
        
        
        while left <= right:
            
            mid = left + (right - left) // 2
            if objects[mid][0] <= timestamp:
                res = objects[mid][1]
                left = mid + 1
                
            else:
                right = mid - 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)