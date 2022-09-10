class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        memo = {}
        
        def dfs(string):
            
            if string in memo:
                return memo[string]
            
            if not string:
                return [""]
            
            local_result = []
            
            for word in wordDict:
                if string.startswith(word):
                    sub_words = dfs(string[len(word):])
                    
                    for w in sub_words:
                        if w:
                            local_result.append(word + ' ' + w)
                        else:
                            local_result.append(word)
            
            memo[string] = local_result
            return memo[string]
    
        return dfs(s)