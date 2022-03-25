class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start = 0
        char_frequency = {}
        matched = 0
        min_len = len(s) + 1
        
        if s == t:
            return s
        
        for char in t:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
        
        for end in range(len(s)):
            right = s[end]
            
            if right in char_frequency:
                char_frequency[right] -= 1
                if char_frequency[right] >= 0:
                    matched += 1
            
            while matched == len(t):
                substring_length = end - start + 1
                if substring_length < min_len:
                    min_len = substring_length
                    substr_start = start
                    
                left = s[start]
                start += 1
                if left in char_frequency:
                    if char_frequency[left] == 0:
                        matched -= 1
                    char_frequency[left] += 1
        
        if min_len == len(s) + 1:
            return ""
        
        return s[substr_start:substr_start + min_len]