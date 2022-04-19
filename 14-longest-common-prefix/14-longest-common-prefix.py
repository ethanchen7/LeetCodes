class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        prefix = strs[0] #flower
        prefixLen = len(prefix)
        
        for i in range(1, len(strs)):
            
            while strs[i][0:prefixLen] != prefix:
                prefixLen -= 1
                prefix = prefix[0:prefixLen]
                
                if prefixLen == 0:
                    return ""
            
        return prefix
            
            