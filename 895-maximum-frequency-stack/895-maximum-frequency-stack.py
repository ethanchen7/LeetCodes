class FreqStack:

    def __init__(self):
        self.stacks = collections.defaultdict(list)
        self.freq = collections.defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        if f > self.max_freq:
            self.max_freq = f
        self.freq[val] += 1
        self.stacks[f].append(val)

    def pop(self) -> int:
        stack_with_max_freq = self.stacks[self.max_freq]
        result = stack_with_max_freq.pop()
        self.freq[result] -= 1
        if not stack_with_max_freq:
            self.max_freq -= 1
        
        return result



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()