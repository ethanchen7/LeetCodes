class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # {a: 1, b: 1, c: 1}
        start = 0
        indices = []
        char_frequency = {}
        matched = 0
        
        for char in p: 
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
        
        for end in range(len(s)):
            right = s[end]
            if right in char_frequency:
                char_frequency[right] -= 1
                if char_frequency[right] == 0:
                    matched += 1

            if (end - start + 1) > len(p):
                left = s[start]
                if left in char_frequency:
                    if char_frequency[left] == 0:
                        matched -= 1
                    char_frequency[left] += 1
                start += 1
                
            if matched == len(char_frequency):
                indices.append(start)
        
        return indices
        