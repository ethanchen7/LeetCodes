class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        curr_idx = 0
        
        for pointer in range(len(nums)):
            if nums[pointer] != nums[curr_idx]:
                curr_idx += 1
                nums[curr_idx] = nums[pointer]
            
            pointer += 1
        
        return curr_idx + 1