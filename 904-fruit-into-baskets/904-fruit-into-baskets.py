class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        # we can only have two of a kind of a fruit at all times
        
        type_frequency = {}
        start = 0
        max_len = 0
        
        for end in range(len(fruits)):
            right = fruits[end]
            if right not in type_frequency:
                type_frequency[right] = 0
            type_frequency[right] += 1
            
            while len(type_frequency) > 2:
                left = fruits[start]
                type_frequency[left] -= 1
                if type_frequency[left] == 0:
                    del type_frequency[left]
                start += 1
            
            curr_len = end - start + 1
            max_len = max(max_len, curr_len)
        
        return max_len