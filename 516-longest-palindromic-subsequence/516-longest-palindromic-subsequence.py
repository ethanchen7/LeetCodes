class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        
        dp = [[-1 for i in range(n)] for j in range(n)]
        
        def dfs(startIndex, endIndex):
            
            if endIndex < startIndex:
                return 0
            
            if startIndex == endIndex:
                return 1
            
            if dp[startIndex][endIndex] == -1:
                if s[startIndex] == s[endIndex]:
                    dp[startIndex][endIndex] = 2 + dfs(startIndex + 1, endIndex - 1)
                    
                else:
                    dp[startIndex][endIndex] = max(dfs(startIndex + 1, endIndex), dfs(startIndex, endIndex - 1))
            
            return dp[startIndex][endIndex]
        
        return dfs(0, n - 1)