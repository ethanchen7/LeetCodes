class OrderedStream:

    def __init__(self, n: int):
        self.map = {i + 1: "" for i in range(n)}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.map[idKey] = value
        if self.map[self.ptr] == "":
            return []
        
        result = []
        i = int(self.ptr)
        while i < len(self.map) + 1 and self.map[i] != "":
            result.append(self.map[i])
            i += 1
        
        self.ptr = i      
        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)