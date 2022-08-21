class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left, right = 0, len(nums) - 1
        
        res = []
        while left <= right:
            
            leftsq = nums[left] ** 2
            rightsq = nums[right] ** 2
            
            if leftsq > rightsq:
                res.append(leftsq)
                left += 1
            
            else:
                res.append(rightsq)
                right -= 1
        
        return res[::-1]