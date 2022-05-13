class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for n in nums:
            
            num = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(num)
            
            result.extend(perms)
            nums.append(num)
        
        return result
            
            