class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_set = set(wordDict)
        
        memo = {}
        
        def dfs(start):
            
            if start in memo:
                return memo[start]
            
            if start >= len(s):
                return True
            
            for i in range(start + 1, len(s) + 1):
                if s[start: i] in word_set:
                    memo[start] = dfs(i)
                    if memo[start]: return True
            
            memo[start] = False
            return memo[start]
        
        return dfs(0)
            