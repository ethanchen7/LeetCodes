class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        counter = Counter(nums)
        
        def permute(perm):
            
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    
                    perm.append(num)
                    counter[num] -= 1
            
                    permute(perm)
                
                    perm.pop()
                    counter[num] += 1
            
        permute([])
        return result