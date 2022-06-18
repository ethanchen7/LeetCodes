class Solution:
    def isValid(self, s: str) -> bool:
        
        paren = {')':'(', '}':'{', ']':'['}
        
        stack = []
        for char in s:
            
            if char not in paren:
                stack.append(char)
            else:
                if stack and stack[-1] == paren[char]:
                    p = stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False