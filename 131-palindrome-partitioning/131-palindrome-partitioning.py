class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        
        def dfs(start, palin):
            
            if start == len(s):
                result.append(palin[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                
                if self.isValid(s[start:end]):
                    palin.append(s[start:end])
                    dfs(end, palin)
                    palin.pop()
                    
        dfs(0, [])
        return result
    
    def isValid(self, string):
        
        left, right = 0, len(string) - 1
        
        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True