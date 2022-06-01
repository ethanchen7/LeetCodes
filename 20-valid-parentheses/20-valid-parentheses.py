class Solution:
    def isValid(self, s: str) -> bool:
        
        paren = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []
        
        for char in s:
            if stack and char in paren:
                p = stack.pop()
                if p != paren[char]:
                    return False
            
            else:
                stack.append(char)
        
        if stack:
            return False
        
        return True