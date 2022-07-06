class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        paren = []
        
        def dfs(openN, closedN):
            
            if openN == closedN == n: 
                result.append("".join(paren))
                return
            
            if openN < n:
                paren.append('(')
                dfs(openN + 1, closedN)
                paren.pop()
            
            if closedN < openN:
                paren.append(')')
                dfs(openN, closedN + 1)
                paren.pop()
            
        dfs(0, 0)
        return result
            
            