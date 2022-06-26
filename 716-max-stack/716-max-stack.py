class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        num = self.stack.pop()
        return num

    def top(self) -> int:
        num = self.stack[-1]
        return num

    def peekMax(self) -> int:
        num = max(self.stack)
        return num

    def popMax(self) -> int:
        num = self.peekMax()
        remove_idx = -1
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == num:
                remove_idx = i
                break
        
        removed = self.stack.pop(remove_idx)
        return removed


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()