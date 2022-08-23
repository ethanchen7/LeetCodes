class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        stack = [] # [#]
        nodes = preorder.split(',')
        
        for n in nodes:
            
            stack.append(n)
            
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        
        
        if len(stack) > 1:
            return False
        
        return stack[0] == '#'
            
        