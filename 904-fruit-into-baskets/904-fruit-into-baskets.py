class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        fruit_freq = {}
        
        start = 0
        max_length = 0
        
        for end in range(len(fruits)):
            right = fruits[end]
            
            if right not in fruit_freq:
                fruit_freq[right] = 0
            fruit_freq[right] += 1
            
            while len(fruit_freq) > 2:
                left = fruits[start]
                
                fruit_freq[left] -= 1
                if fruit_freq[left] == 0:
                    del fruit_freq[left]
                
                start += 1
            
            length = end - start + 1
            max_length = max(length, max_length)
        
        return max_length