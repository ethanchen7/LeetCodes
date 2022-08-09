class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [-1 for i in range(len(s))]
        
        def dfs(idx):
            
            if idx == len(s):
                return 1
            
            if s[idx] == "0":
                return 0
            
            if idx == len(s) - 1:
                return 1
            
            if dp[idx] != -1:
                return dp[idx]
            
            dp[idx] = dfs(idx + 1)
            if int(s[idx: idx + 2]) <= 26:
                dp[idx] += dfs(idx + 2)
            
            return dp[idx]
        
        return dfs(0)