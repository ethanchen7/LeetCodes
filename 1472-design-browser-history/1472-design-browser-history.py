class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        while self.current != len(self.stack) - 1: # clear the stack's forward history
            self.stack.pop()
        self.stack.append(url)
        self.current = len(self.stack) - 1
        
    def back(self, steps: int) -> str:
        new_pos = self.current - steps
        if new_pos < 0:
            self.current = 0
            return self.stack[self.current]
        
        self.current = new_pos
        return self.stack[self.current]

    def forward(self, steps: int) -> str:
        new_pos = self.current + steps
        if new_pos >= len(self.stack):
            self.current = len(self.stack) - 1
            return self.stack[self.current]
        
        self.current = new_pos
        return self.stack[self.current]
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)