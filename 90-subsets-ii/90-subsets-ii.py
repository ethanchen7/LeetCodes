class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        subsets.append([])
        
        nums.sort()
        
        start, end = 0, 0
        
        for i in range(len(nums)):
            
            start = 0
            
            if i > 0 and nums[i] == nums[i - 1]:
                start = end + 1
            
            end = len(subsets) - 1
            
            for j in range(start, end + 1):
                set1 = list(subsets[j])
                set1.append(nums[i])
                subsets.append(set1)
        
        return subsets