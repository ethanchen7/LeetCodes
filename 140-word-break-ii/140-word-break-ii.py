class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)
        result = []
        
        # memo = {}
        def dfs(start, words):
            
            
            if start == len(s):
                result.append(" ".join(words))
                return
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    
                    words.append(s[start:end])
                    
                    dfs(end, words)
                        
                    words.pop()
            
        dfs(0, [])
        return result