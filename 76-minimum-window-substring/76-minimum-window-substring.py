class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        matched = 0 # must be len(t_frequency)
        start = 0
        min_window_len = len(s)
        min_substr = ""
        
        
        t_frequency = {}
        for char in t:
            if char not in t_frequency:
                t_frequency[char] = 0
            t_frequency[char] += 1
            
        for end in range(len(s)):
            right = s[end]
            if right in t_frequency:
                t_frequency[right] -= 1
                if t_frequency[right] == 0:
                    matched += 1
            
            while matched == len(t_frequency):
                # save the window_size
                window_size = end - start + 1
                if window_size <= min_window_len:
                    min_window_len = window_size
                    min_substr = s[start:end + 1]

                # shrink the window
                left = s[start]
                if left in t_frequency:
                    if t_frequency[left] == 0:
                        matched -= 1
                    t_frequency[left] += 1
                    
                
                start += 1
        
        return min_substr