class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}
        for n in nums:
            if n in seen:
                return True
            seen[n] = 1
            
        return False