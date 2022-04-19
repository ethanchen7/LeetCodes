class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        needleLen = len(needle)
        
        for i in range(0, len(haystack) - needleLen + 1):
        
            if haystack[i:i+needleLen] == needle:
                return i
        
        return -1