class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # recursion tree
        
        #      abbreviate, or don't abbreviate
        #  index0                  1      word
        # index1               2     1ord
        # index2            3     2rd  
        # index3         4  3d  2r1  2rd
        
        result = []
        n = len(word)
        
        def dfs(idx, curr):
            
            if idx == n:
                result.append(curr)
                return
            
            dfs(idx + 1, curr + word[idx])
            
            for i in range(1, n - idx + 1):
                if not curr or not curr[-1].isnumeric():
                    dfs(idx + i, curr + str(i))
                else:
                    return
        
        dfs(0, "")
        return result