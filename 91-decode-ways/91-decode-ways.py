class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = collections.defaultdict(int)
        
        def dfs(idx):
                        
            if idx in memo:
                return memo[idx]
            
            if idx == len(s): 
                return 1
            
            if s[idx] == "0": # if it starts as a 0, we can't finish it
                return 0
            
            if idx == len(s) - 1: # len - 1 because we will check substring[i:i+2]
                return 1
            
            count = dfs(idx + 1) # one digit
            if int(s[idx:idx + 2]) <= 26: # two digit
                count += dfs(idx + 2)
            
            memo[idx] = count
            return memo[idx]
        
        return dfs(0)
            
            