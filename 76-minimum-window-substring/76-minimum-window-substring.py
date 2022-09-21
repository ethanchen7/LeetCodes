class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        char_frequency = Counter(t)
        start = 0
        min_window = math.inf
        result = ""
        matched = 0
        
        for end in range(len(s)):
            right = s[end]
            if right in char_frequency:
                char_frequency[right] -= 1
                if char_frequency[right] == 0:
                    matched += 1
            
            while matched == len(char_frequency):
                window = end - start + 1
                if window <= min_window:
                    min_window = min(min_window, window)
                    result = s[start:end + 1]
                
                
                left = s[start]
                if left in char_frequency:
                    if char_frequency[left] == 0:
                        matched -= 1
                    char_frequency[left] += 1
                start += 1
        
        return result