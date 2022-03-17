class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        type_frequency = {}
        start = 0
        maxFruits = 0
        
        for end in range(0, len(fruits)):
            if fruits[end] not in type_frequency:
                type_frequency[fruits[end]] = 0
            type_frequency[fruits[end]] += 1
        
            while len(type_frequency) > 2:
                left = fruits[start]
                type_frequency[left] -= 1
                if type_frequency[left] == 0:
                    del type_frequency[left]
                start += 1
            
            maxFruits = max(maxFruits, end - start + 1)
        
        return maxFruits