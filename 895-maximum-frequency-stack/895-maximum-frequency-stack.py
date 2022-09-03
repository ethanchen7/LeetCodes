class FreqStack:

    def __init__(self):
        self.frequencies = collections.defaultdict(int)
        self.stacks = collections.defaultdict(list)
        self.maxFreq = 0

        # 5: 3, 7: 2, 4: 1
        # 1: [5, 7, 4], 2: [5, 7], 3: [5]
        # maxFreq = 3
        
    def push(self, val: int) -> None:
        self.frequencies[val] += 1
        self.maxFreq = max(self.maxFreq, self.frequencies[val])
        self.stacks[self.frequencies[val]].append(val)
        
    def pop(self) -> int:
        max_stack = self.stacks[self.maxFreq]

        res = max_stack.pop()
        if len(self.stacks[self.maxFreq]) == 0:
            del self.stacks[self.maxFreq]
            self.maxFreq -= 1
        self.frequencies[res] -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()