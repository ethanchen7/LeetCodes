class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        memo = {}
        
        def dfs(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and dfs(end): # check if the substring exists and pass in the end pointer to the dfs
                    memo[start]=True
                    return memo[start]
            
            memo[start] = False
            return memo[start]
        
        return dfs(0)