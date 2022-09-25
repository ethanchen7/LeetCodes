class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        result = []
        def dfs(idx, string):
            
            if idx == len(word):
                result.append("".join(string))
                return
            
            if not string:
                dfs(idx + 1, string + [str(1)])
                dfs(idx + 1, string + [str(word[idx])])
            
            elif string[-1].isnumeric():
                string[-1] = str(int(string[-1]) + 1)
                dfs(idx + 1, string)
                string[-1] = str(int(string[-1]) - 1)
                dfs(idx + 1, string + [str(word[idx])])
            
            else:
                dfs(idx + 1, string + [str(1)])
                dfs(idx + 1, string + [str(word[idx])])
        
        
        dfs(0, [])
        return result
            
            