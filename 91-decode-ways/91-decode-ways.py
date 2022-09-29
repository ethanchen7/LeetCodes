class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        
        def dfs(idx):
            
            if idx in memo:
                return memo[idx]
            
            if idx > len(s):
                return 0
            
            if idx == len(s):
                return 1
            
            if s[idx] == '0':
                return 0
            
            one_group = dfs(idx + 1)
            
            two_group = 0
            if 10 <= int(s[idx: idx + 2]) <= 26:
                two_group += dfs(idx + 2)
            
            memo[idx]=one_group + two_group
            return memo[idx]
        
        return dfs(0)