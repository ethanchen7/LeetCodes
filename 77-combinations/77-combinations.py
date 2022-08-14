class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        comb = []
        
        def generate(i):
            
            if len(comb) == k:
                result.append(comb[:])
                return
            
            for j in range(i, n + 1):
                
                comb.append(j)
                generate(j + 1)
                comb.pop()
        
        generate(1)
        return result
                