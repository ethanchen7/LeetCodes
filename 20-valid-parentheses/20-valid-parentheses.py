class Solution:
    def isValid(self, s: str) -> bool:
        
        paren = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        
        stack = []
        
        for char in s:
            
            if char in paren:
                if stack:
                    compare = stack.pop()
                    if compare != paren[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        return True
        