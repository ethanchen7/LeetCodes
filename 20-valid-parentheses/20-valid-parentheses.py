class Solution:
    def isValid(self, s: str) -> bool:
        
        paren = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        if len(s) < 2:
            return False
        
        stack = []
        for p in s:
            if p in paren:
                if stack:
                    char = stack.pop()
                else:
                    return False
                if paren[p] != char:
                    return False
            else:
                stack.append(p)
        
        if stack:
            return False
        return True