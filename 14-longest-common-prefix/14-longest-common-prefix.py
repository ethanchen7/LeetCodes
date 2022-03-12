class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0]
        preLen = len(prefix)
        
        for i in range(1, len(strs)):
           
            while strs[i][0:preLen] != prefix:   
                preLen -= 1
                prefix = prefix[0:preLen]
                
                if preLen == 0:
                    return ""

        return prefix
            
        
        
        
        