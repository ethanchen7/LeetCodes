class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_hash = {}
        
        for i,char in enumerate(s):
            if char not in s_hash:
                s_hash[char] = []
            s_hash[char].append(i)
            
        
        t_hash = {}
        for i,char in enumerate(t):
            if char not in t_hash:
                t_hash[char] = []
            t_hash[char].append(i)
        
        
        return list(s_hash.values()) == list(t_hash.values())
            