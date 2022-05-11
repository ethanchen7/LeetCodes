class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        
        if len(nums) == 1:
            return [nums[:]] #returns a copy of nums, because we are going to mutate nums
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums) # each time, nums is shorter by 1 until we hit our base case
            
            for perm in perms:
                perm.append(n)
            
            result.extend(perms)
            nums.append(n)
        
        return result
            
        