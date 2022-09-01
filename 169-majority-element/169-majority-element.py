class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Boyer - Moore
        # keep a voting variable that will increment as long as the number is the same
        # decrement when there is a different number
        # set the current number to the current number once we hit a count of 0
        count = 0
        candidate = None
        
        for n in nums:
            
            if count == 0:
                candidate = n
            
            if n == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate