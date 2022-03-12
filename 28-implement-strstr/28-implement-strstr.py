class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        window = len(needle)
        
        if not needle:
            return 0
        
        for i in range(0, len(haystack) - window + 1):
            if haystack[i:i+window] == needle:
                return i
        
        return -1
    

        