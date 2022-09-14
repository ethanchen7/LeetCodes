class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        
        def dfs(idx):
            
            if idx in memo:
                return memo[idx]
            
            if idx == len(s):
                return 1
            
            if idx > len(s):
                return 0
            
            if s[idx] == '0':
                return 0
            
            one_way = dfs(idx + 1)
            
            two_way = 0
            if 10 <= int(s[idx:idx+2]) <= 26:
                two_way += dfs(idx + 2)
            
            memo[idx] = one_way + two_way
            return memo[idx]
        
        return dfs(0)