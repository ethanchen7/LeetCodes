class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_frequency = {}
        t_frequency = {}
        
        for char in s:
            if char not in s_frequency:
                s_frequency[char] = 0
            s_frequency[char] += 1
            
        for char in t:
            if char not in t_frequency:
                t_frequency[char] = 0
            t_frequency[char] += 1
        
        return t_frequency == s_frequency