class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        currIndex = 0
        
        for pointer in range(1, len(nums)):
            
            if nums[pointer] != nums[currIndex]:
                currIndex += 1
                nums[currIndex] = nums[pointer]
            
        return currIndex + 1