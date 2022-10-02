class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}
        
        for i,n in enumerate(nums):
            
            diff = target - n
            if diff in nums_dict:
                return [nums_dict[diff], i]
            
            nums_dict[n] = i