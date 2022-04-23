class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        currPosition, runner = 0, 0
        
        while runner < len(nums):
            
            if nums[runner] != nums[currPosition]:
                currPosition += 1
                nums[currPosition] = nums[runner]
                     
            runner += 1
        
        return currPosition + 1
    
