class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        part = []
        
        def dfs(i):

            if i >= len(s): # reached the end of the check, append what we have
                result.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.valid(s[i: j + 1]):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return result
    
    
    def valid(self, substring):
        
        if not substring: return False
        
        left = 0
        right = len(substring) - 1
        
        while left <= right:
            
            if substring[left] != substring[right]:
                return False
            
            left += 1
            right -= 1
            
        return True