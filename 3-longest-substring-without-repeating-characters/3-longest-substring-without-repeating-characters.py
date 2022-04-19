class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        char_frequency = {}
        max_len = 0
        
        for end in range(len(s)):
            right = s[end]
            if right not in char_frequency:
                char_frequency[right] = 0
            char_frequency[right] += 1
            
            while char_frequency[right] > 1:
                left = s[start]
                char_frequency[left] -= 1
                start += 1
            
            curr_len = end - start + 1
            max_len = max(max_len, curr_len)
        
        return max_len