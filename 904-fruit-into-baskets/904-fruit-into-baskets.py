class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        char_frequency = {}
        start = 0
        max_length = 0
        
        for end in range(len(fruits)):
            if fruits[end] not in char_frequency:
                char_frequency[fruits[end]] = 0
            char_frequency[fruits[end]] += 1
            
            while len(char_frequency) > 2:
                left = fruits[start]
                char_frequency[left] -= 1
                if char_frequency[left] == 0:
                    del char_frequency[left]
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length
             
            