class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        i = 0
        
        while i < n:
            j = nums[i] - 1
            
            if nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            
            else:
                i += 1
        
        result = []
        for i in range(n):
            if nums[i] != i + 1:
                result.append(nums[i])
        
        return result