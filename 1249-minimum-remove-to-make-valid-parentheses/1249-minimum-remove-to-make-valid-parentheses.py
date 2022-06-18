class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        S = list(s)
        
        for i in range(len(S)):
            
            if S[i] == "(":
                stack.append(i)
            
            elif S[i] == ")":
                if stack:
                    stack.pop()
                else:
                    S[i] = ""
        
        for j in stack:
            S[j] = ""
        
        return ("").join(S)
                    