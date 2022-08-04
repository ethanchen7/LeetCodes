class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        result = []
        ip_string = ""
        
        if len(s) > 12:
            return result
        
        def dfs(i, dots, ip_string):
            
            if dots == 4 and i == len(s):
                result.append(ip_string[:-1])
                return
            
            if dots > 4:
                return
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) <= 255 and (i == j or s[i] != "0"):
                    dfs(j + 1, dots + 1, ip_string + s[i:j+1] + ".")
            
    
        dfs(0, 0, ip_string)
        return result